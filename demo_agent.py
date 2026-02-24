"""
Example usage of the AI Todo Agent.

This script demonstrates how to use the AI Todo Agent programmatically.
"""

import sys
import os

# Add the project root to the path to import modules correctly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from src.services.task_service import TaskService
from src.agents.todo_agent import TodoAgent

def demo_agent():
    """Demonstrate the capabilities of the AI Todo Agent."""
    # Initialize the service and agent
    service = TaskService()
    agent = TodoAgent(service)
    
    print("🤖 AI Todo Agent Demo")
    print("=" * 30)
    
    # Demonstrate adding tasks
    print("\n1. Adding tasks:")
    print("User: add task Buy groceries with description Need to buy milk, eggs, and bread")
    response = agent.process_command("add task Buy groceries with description Need to buy milk, eggs, and bread")
    print(f"Agent: {response}")
    
    print("\nUser: add task Study for exam")
    response = agent.process_command("add task Study for exam")
    print(f"Agent: {response}")
    
    print("\nUser: create task Call mom")
    response = agent.process_command("create task Call mom")
    print(f"Agent: {response}")
    
    # Demonstrate viewing tasks
    print("\n2. Viewing tasks:")
    print("User: show my tasks")
    response = agent.process_command("show my tasks")
    print(f"Agent: {response}")
    
    # Demonstrate marking a task as complete
    print("\n3. Updating task status:")
    print("User: mark task 1 as complete")
    response = agent.process_command("mark task 1 as complete")
    print(f"Agent: {response}")
    
    # Demonstrate updating a task
    print("\n4. Updating a task:")
    print("User: update task 2 with title Study for math exam")
    response = agent.process_command("update task 2 with title Study for math exam")
    print(f"Agent: {response}")
    
    # Show updated tasks
    print("\n5. View updated tasks:")
    print("User: what do I have to do?")
    response = agent.process_command("what do I have to do?")
    print(f"Agent: {response}")
    
    # Demonstrate deleting a task
    print("\n6. Deleting a task:")
    print("User: delete task 3")
    response = agent.process_command("delete task 3")
    print(f"Agent: {response}")
    
    # Final view
    print("\n7. Final task list:")
    print("User: show tasks")
    response = agent.process_command("show tasks")
    print(f"Agent: {response}")
    
    print("\n✅ Demo completed!")

if __name__ == "__main__":
    demo_agent()