"""Task data model for Phase I console todo application.

This module defines the Task entity and TaskStatus enum used throughout the application.
"""

from dataclasses import dataclass
from enum import Enum


class TaskStatus(Enum):
    """Task completion status.

    Attributes:
        INCOMPLETE: Task has not been completed (default state)
        COMPLETE: Task has been completed
    """
    INCOMPLETE = "Incomplete"
    COMPLETE = "Complete"


@dataclass
class Task:
    """Represents a single todo task.

    Attributes:
        id: Unique numeric identifier (auto-generated, sequential)
        title: Brief description of what needs to be done (1-500 chars, required)
        description: Optional detailed information about the task (0-2000 chars)
        status: Task completion status (INCOMPLETE or COMPLETE)
    """
    id: int
    title: str
    description: str
    status: TaskStatus

    def __str__(self) -> str:
        """Return human-readable string representation of the task."""
        status_str = self.status.value
        desc_preview = (self.description[:50] + "...") if len(self.description) > 50 else self.description
        return f"Task({self.id}, '{self.title}', status={status_str}, desc='{desc_preview}')"
