"""CLI menu interface for the todo application.

This module handles all user interaction through the command-line interface.
"""

from services.task_service import TaskService, TaskNotFoundError, InvalidInputError


def display_menu() -> None:
    """Display the main menu options."""
    print("\n" + "=" * 33)
    print("   Todo List - Main Menu")
    print("=" * 33)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
    print()


def get_menu_choice() -> int:
    """Get and validate user's menu choice.

    Returns:
        Integer between 1-6 representing the user's choice

    Note:
        Keeps prompting until valid input is received
    """
    while True:
        try:
            choice = input("Enter your choice (1-6): ").strip()
            choice_int = int(choice)

            if 1 <= choice_int <= 6:
                return choice_int
            else:
                display_error("Invalid option. Please select a number from the menu.")
        except ValueError:
            display_error("Invalid option. Please select a number from the menu.")


def display_error(message: str) -> None:
    """Display an error message to the user.

    Args:
        message: The error message to display
    """
    print(f"\n✗ Error: {message}")
    print()


def display_success(message: str) -> None:
    """Display a success message to the user.

    Args:
        message: The success message to display
    """
    print(f"\n✓ {message}")
    print()


def handle_add_task(service: TaskService) -> None:
    """Handle the add task operation.

    Prompts user for task title and description, then adds the task.

    Args:
        service: The TaskService instance to use for adding tasks
    """
    print("\n--- Add New Task ---\n")

    # Get title
    title = input("Enter task title: ").strip()

    # Validate title
    if not title:
        display_error("Task title cannot be empty")
        return

    # Get description (optional)
    description = input("Enter task description (optional, press Enter to skip): ").strip()

    try:
        # Add task
        task = service.add_task(title, description)
        display_success(f"Task added successfully (ID: {task.id})")
    except InvalidInputError as e:
        display_error(str(e))


def handle_view_tasks(service: TaskService) -> None:
    """Handle the view tasks operation.

    Displays all tasks with their ID, status, title, and description.

    Args:
        service: The TaskService instance to use for retrieving tasks
    """
    print("\n" + "=" * 33)
    print("   Your Tasks")
    print("=" * 33)
    print()

    tasks = service.get_all_tasks()

    if not tasks:
        print("No tasks found. Your list is empty.")
        print()
        return

    # Count tasks by status
    complete_count = sum(1 for t in tasks if t.status.value == "Complete")
    incomplete_count = len(tasks) - complete_count

    # Display each task
    for task in tasks:
        status_indicator = f"[{task.status.value}]"
        print(f"ID: {task.id} | {status_indicator} | {task.title}")

        if task.description:
            print(f"         Description: {task.description}")

        print()  # Blank line between tasks

    # Display summary
    print(f"Total: {len(tasks)} task{'s' if len(tasks) != 1 else ''} "
          f"({complete_count} complete, {incomplete_count} incomplete)")
    print()


def handle_toggle_status(service: TaskService) -> None:
    """Handle the toggle task status operation.

    Prompts user for task ID and toggles its completion status.

    Args:
        service: The TaskService instance to use for toggling status
    """
    print("\n--- Mark Complete/Incomplete ---\n")

    # Get task ID
    task_id_input = input("Enter task ID: ").strip()

    # Validate ID format
    try:
        task_id = int(task_id_input)
    except ValueError:
        display_error("Invalid task ID. Please enter a number.")
        return

    try:
        # Toggle status
        task = service.toggle_status(task_id)
        display_success(f"Task {task_id} marked as {task.status.value}")
    except TaskNotFoundError:
        display_error(f"Task with ID {task_id} not found")


def handle_update_task(service: TaskService) -> None:
    """Handle the update task operation.

    Prompts user for task ID and new title/description.

    Args:
        service: The TaskService instance to use for updating tasks
    """
    print("\n--- Update Task ---\n")

    # Get task ID
    task_id_input = input("Enter task ID: ").strip()

    # Validate ID format
    try:
        task_id = int(task_id_input)
    except ValueError:
        display_error("Invalid task ID. Please enter a number.")
        return

    try:
        # Get current task to show user
        current_task = service.get_task_by_id(task_id)
        print(f"\nCurrent title: {current_task.title}")
        print(f"Current description: {current_task.description if current_task.description else '(empty)'}\n")

        # Get new title (optional)
        new_title_input = input("Enter new title (press Enter to keep current): ").strip()
        new_title = new_title_input if new_title_input else None

        # Get new description (optional)
        new_desc_input = input("Enter new description (press Enter to keep current): ").strip()
        new_description = new_desc_input if new_desc_input != "" else None

        # If user pressed Enter for both, nothing to update
        if new_title is None and new_description is None:
            print("\nNo changes made.")
            return

        # Update task
        service.update_task(task_id, new_title, new_description)
        display_success(f"Task {task_id} updated successfully")

    except TaskNotFoundError:
        display_error(f"Task with ID {task_id} not found")
    except InvalidInputError as e:
        display_error(str(e))


def handle_delete_task(service: TaskService) -> None:
    """Handle the delete task operation.

    Prompts user for task ID and deletes the task.

    Args:
        service: The TaskService instance to use for deleting tasks
    """
    print("\n--- Delete Task ---\n")

    # Get task ID
    task_id_input = input("Enter task ID: ").strip()

    # Validate ID format
    try:
        task_id = int(task_id_input)
    except ValueError:
        display_error("Invalid task ID. Please enter a number.")
        return

    try:
        # Delete task
        service.delete_task(task_id)
        display_success(f"Task {task_id} deleted successfully")
    except TaskNotFoundError:
        display_error(f"Task with ID {task_id} not found")
