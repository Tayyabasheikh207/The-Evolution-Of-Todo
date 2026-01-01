"""Task service for managing todo tasks.

This module provides business logic for CRUD operations on tasks with in-memory storage.
"""

from typing import Optional
from models.task import Task, TaskStatus


class TaskNotFoundError(Exception):
    """Raised when a task with the specified ID does not exist."""
    pass


class InvalidInputError(Exception):
    """Raised when user input fails validation."""
    pass


class TaskService:
    """Service class for managing tasks with in-memory storage.

    This service provides CRUD operations for tasks and maintains
    an in-memory dictionary for storage with sequential ID generation.

    Attributes:
        _tasks: Dictionary mapping task IDs to Task objects
        _next_id: Counter for generating sequential task IDs
    """

    def __init__(self) -> None:
        """Initialize the task service with empty storage."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task to the storage.

        Args:
            title: Task title (1-500 characters, required)
            description: Optional task description (0-2000 characters)

        Returns:
            The newly created Task object with auto-generated ID

        Raises:
            InvalidInputError: If title is empty after stripping whitespace
        """
        # Validate and clean title
        title = title.strip()
        if not title:
            raise InvalidInputError("Task title cannot be empty")

        # Truncate title if exceeds max length
        if len(title) > 500:
            title = title[:497] + "..."

        # Truncate description if exceeds max length
        if len(description) > 2000:
            description = description[:1997] + "..."

        # Generate ID and create task
        task_id = self._next_id
        self._next_id += 1

        task = Task(
            id=task_id,
            title=title,
            description=description,
            status=TaskStatus.INCOMPLETE
        )

        # Store task
        self._tasks[task_id] = task
        return task

    def get_all_tasks(self) -> list[Task]:
        """Retrieve all tasks from storage.

        Returns:
            List of all Task objects, ordered by ID
        """
        return list(self._tasks.values())

    def get_task_by_id(self, task_id: int) -> Task:
        """Retrieve a task by its ID.

        Args:
            task_id: The unique identifier of the task

        Returns:
            The Task object with the specified ID

        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
        return self._tasks[task_id]

    def toggle_status(self, task_id: int) -> Task:
        """Toggle a task's completion status.

        Switches status between INCOMPLETE and COMPLETE.

        Args:
            task_id: The unique identifier of the task

        Returns:
            The updated Task object

        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        task = self.get_task_by_id(task_id)  # Raises TaskNotFoundError if not found

        if task.status == TaskStatus.INCOMPLETE:
            task.status = TaskStatus.COMPLETE
        else:
            task.status = TaskStatus.INCOMPLETE

        return task

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None
    ) -> Task:
        """Update a task's title and/or description.

        Args:
            task_id: The unique identifier of the task
            title: New title (None = no change)
            description: New description (None = no change)

        Returns:
            The updated Task object

        Raises:
            TaskNotFoundError: If no task exists with the given ID
            InvalidInputError: If provided title is empty after stripping
        """
        task = self.get_task_by_id(task_id)  # Raises TaskNotFoundError if not found

        # Update title if provided
        if title is not None:
            title = title.strip()
            if not title:
                raise InvalidInputError("Task title cannot be empty")

            # Truncate if exceeds max length
            if len(title) > 500:
                title = title[:497] + "..."

            task.title = title

        # Update description if provided
        if description is not None:
            # Truncate if exceeds max length
            if len(description) > 2000:
                description = description[:1997] + "..."

            task.description = description

        return task

    def delete_task(self, task_id: int) -> None:
        """Delete a task from storage.

        Args:
            task_id: The unique identifier of the task to delete

        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"Task with ID {task_id} not found")

        del self._tasks[task_id]
