"""
AI Todo Agent for natural language interaction with the todo application.

This module implements an intelligent agent that can understand natural language
commands to perform CRUD operations on tasks.
"""

import re
import sys
import os
from typing import Dict, List, Optional, Tuple

# Add the src directory to the path to import modules correctly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services.task_service import TaskService, TaskNotFoundError, InvalidInputError
from models.task import Task, TaskStatus


class TodoAgent:
    """
    An AI agent that interprets natural language commands to manage tasks.
    
    The agent can understand various ways of expressing commands like:
    - Adding tasks: "add task buy groceries", "create task study for exam"
    - Viewing tasks: "show me my tasks", "what do I have to do?"
    - Updating tasks: "update task 1 with new title", "change description of task 2"
    - Deleting tasks: "delete task 3", "remove task 4"
    - Toggling status: "mark task 1 as complete", "complete task 2"
    """
    
    def __init__(self, service: TaskService):
        """
        Initialize the agent with a task service.
        
        Args:
            service: The TaskService instance to interact with
        """
        self.service = service
        
    def process_command(self, command: str) -> str:
        """
        Process a natural language command and execute the corresponding action.
        
        Args:
            command: Natural language command from the user
            
        Returns:
            Response string indicating the result of the command
        """
        command_lower = command.lower().strip()
        
        # Determine the intent based on keywords
        if self._contains_keywords(command_lower, ['add', 'create', 'new task', 'make task']):
            return self._handle_add_task(command_lower)
        elif self._contains_keywords(command_lower, ['view', 'show', 'list', 'see', 'what do', 'my tasks', 'all tasks']):
            return self._handle_view_tasks(command_lower)
        elif self._contains_keywords(command_lower, ['update', 'change', 'modify', 'edit']):
            return self._handle_update_task(command_lower)
        elif self._contains_keywords(command_lower, ['delete', 'remove', 'kill', 'erase']):
            return self._handle_delete_task(command_lower)
        elif self._contains_keywords(command_lower, ['complete', 'done', 'finish', 'mark', 'finished']):
            return self._handle_toggle_status(command_lower)
        elif self._contains_keywords(command_lower, ['help', 'commands', 'options']):
            return self._show_help()
        else:
            return "I didn't understand that command. Type 'help' to see available commands."
    
    def _contains_keywords(self, text: str, keywords: List[str]) -> bool:
        """
        Check if the text contains any of the specified keywords.
        
        Args:
            text: Text to search in
            keywords: List of keywords to look for
            
        Returns:
            True if any keyword is found, False otherwise
        """
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in keywords)
    
    def _extract_task_info(self, command: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Extract title and description from a command string.
        
        Args:
            command: Command string to extract info from
            
        Returns:
            Tuple of (title, description) or (None, None) if not found
        """
        # Look for patterns like "add task [title]" or "create task [title]"
        patterns = [
            r'(?:add|create|new|make)\s+(?:task|todo)\s+(.+?)(?:\s+with\s+description\s+(.+)|$)',
            r'(?:add|create|new|make)\s+(?:task|todo)\s+(.+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, command, re.IGNORECASE)
            if match:
                groups = match.groups()
                title = groups[0].strip()
                
                # If there's a description group and it's not None
                description = groups[1].strip() if len(groups) > 1 and groups[1] else ""
                
                # Clean up the title if it contains extra phrases
                if 'with description' in title:
                    title = title.split('with description')[0].strip()
                    
                return title, description
        
        return None, None
    
    def _extract_task_id(self, command: str) -> Optional[int]:
        """
        Extract task ID from a command string.
        
        Args:
            command: Command string to extract ID from
            
        Returns:
            Task ID if found, None otherwise
        """
        # Look for numbers in the command which could be the task ID
        numbers = re.findall(r'\b\d+\b', command)
        if numbers:
            try:
                return int(numbers[0])
            except ValueError:
                return None
        return None
    
    def _handle_add_task(self, command: str) -> str:
        """
        Handle adding a new task based on the command.
        
        Args:
            command: Command string for adding a task
            
        Returns:
            Response string indicating the result
        """
        title, description = self._extract_task_info(command)
        
        if not title:
            # Try to extract everything after the command words
            parts = command.split()
            if len(parts) > 2:
                title = ' '.join(parts[2:])  # Skip 'add' and 'task'
            else:
                return "Please specify a task title. Example: 'add task buy groceries'"
        
        try:
            task = self.service.add_task(title, description or "")
            return f"Added task '{task.title}' with ID {task.id}."
        except InvalidInputError as e:
            return f"Could not add task: {str(e)}"
    
    def _handle_view_tasks(self, command: str) -> str:
        """
        Handle viewing tasks based on the command.
        
        Args:
            command: Command string for viewing tasks
            
        Returns:
            Response string with the list of tasks
        """
        tasks = self.service.get_all_tasks()
        
        if not tasks:
            return "You have no tasks in your list."
        
        response = f"You have {len(tasks)} task{'s' if len(tasks) != 1 else ''}:\n"
        complete_count = sum(1 for t in tasks if t.status == TaskStatus.COMPLETE)
        incomplete_count = len(tasks) - complete_count
        
        for task in tasks:
            status = "X" if task.status == TaskStatus.COMPLETE else "O"
            response += f"[{status}] [{task.id}] {task.title}\n"
            if task.description:
                response += f"    Description: {task.description}\n"
        
        response += f"\nSummary: {complete_count} completed, {incomplete_count} pending"
        return response
    
    def _handle_update_task(self, command: str) -> str:
        """
        Handle updating a task based on the command.
        
        Args:
            command: Command string for updating a task
            
        Returns:
            Response string indicating the result
        """
        task_id = self._extract_task_id(command)
        if not task_id:
            return "Please specify a task ID. Example: 'update task 1 with new title'"
        
        # Try to extract new title or description
        title_match = re.search(r'(?:to|with|new)\s+title\s+(.+?)(?:\s+and|$)', command, re.IGNORECASE)
        desc_match = re.search(r'(?:with|new)\s+description\s+(.+)', command, re.IGNORECASE)
        
        new_title = title_match.group(1).strip() if title_match else None
        new_description = desc_match.group(1).strip() if desc_match else None
        
        # If we couldn't extract from structured format, try to get remaining text
        if not new_title and not new_description:
            # Look for text after the task ID
            parts = command.split()
            try:
                id_idx = parts.index(str(task_id))
                if id_idx + 1 < len(parts):
                    # Assume the rest is the new title
                    new_title = ' '.join(parts[id_idx + 1:])
            except ValueError:
                pass
        
        try:
            updated_task = self.service.update_task(task_id, new_title, new_description)
            changes = []
            if new_title:
                changes.append(f"title to '{updated_task.title}'")
            if new_description is not None:
                changes.append(f"description to '{updated_task.description}'")
            
            if changes:
                return f"Updated task {task_id}: {' and '.join(changes)}."
            else:
                return "No updates were specified. Please provide a new title or description."
        except TaskNotFoundError:
            return f"Task with ID {task_id} not found."
        except InvalidInputError as e:
            return f"Could not update task: {str(e)}"
    
    def _handle_delete_task(self, command: str) -> str:
        """
        Handle deleting a task based on the command.
        
        Args:
            command: Command string for deleting a task
            
        Returns:
            Response string indicating the result
        """
        task_id = self._extract_task_id(command)
        if not task_id:
            return "Please specify a task ID. Example: 'delete task 1'"
        
        try:
            self.service.delete_task(task_id)
            return f"Deleted task {task_id}."
        except TaskNotFoundError:
            return f"Task with ID {task_id} not found."
    
    def _handle_toggle_status(self, command: str) -> str:
        """
        Handle toggling task status based on the command.
        
        Args:
            command: Command string for toggling task status
            
        Returns:
            Response string indicating the result
        """
        task_id = self._extract_task_id(command)
        if not task_id:
            return "Please specify a task ID. Example: 'mark task 1 as complete'"
        
        try:
            task = self.service.toggle_status(task_id)
            status = "completed" if task.status == TaskStatus.COMPLETE else "marked as incomplete"
            return f"Task {task_id} {status}."
        except TaskNotFoundError:
            return f"Task with ID {task_id} not found."
    
    def _show_help(self) -> str:
        """
        Show help information with available commands.
        
        Returns:
            Help text with command examples
        """
        help_text = """
Available commands:
- Add task: "add task [title]", "create task [title] with description [desc]"
- View tasks: "show tasks", "list all tasks", "what do I have to do?"
- Update task: "update task [id] with title [new title]", "change task [id] description [new desc]"
- Delete task: "delete task [id]", "remove task [id]"
- Mark complete: "mark task [id] as complete", "complete task [id]", "finish task [id]"
- Help: "help", "show commands"

Examples:
- "add task buy groceries with description milk and eggs"
- "show my tasks"
- "mark task 1 as complete"
- "delete task 2"
        """
        return help_text.strip()


def run_agent_interface():
    """
    Run a simple command-line interface for the AI agent.
    """
    service = TaskService()
    agent = TodoAgent(service)
    
    print("=" * 50)
    print("  AI Todo Agent - Natural Language Interface")
    print("=" * 50)
    print("Type your commands in natural language or 'quit' to exit.")
    print("Type 'help' to see available commands.\n")
    
    while True:
        try:
            command = input("You: ").strip()
            
            if command.lower() in ['quit', 'exit', 'bye']:
                print("AI Agent: Goodbye!")
                break
                
            if not command:
                continue
                
            response = agent.process_command(command)
            print(f"AI Agent: {response}\n")
            
        except KeyboardInterrupt:
            print("\nAI Agent: Goodbye!")
            break
        except Exception as e:
            print(f"AI Agent: An error occurred: {str(e)}")


if __name__ == "__main__":
    run_agent_interface()