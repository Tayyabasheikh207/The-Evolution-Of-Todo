"""Main entry point for the Phase I console todo application.

This module contains the main loop that displays the menu and dispatches
user choices to the appropriate handlers.
"""

from services.task_service import TaskService
from cli.menu import (
    display_menu,
    get_menu_choice,
    handle_add_task,
    handle_view_tasks,
    handle_update_task,
    handle_delete_task,
    handle_toggle_status,
    display_error
)


def main() -> None:
    """Main application loop.

    Initializes the task service and runs the menu loop until user exits.
    """
    # Initialize service
    service = TaskService()

    # Main loop
    while True:
        try:
            # Display menu and get choice
            display_menu()
            choice = get_menu_choice()

            # Dispatch based on choice
            if choice == 1:
                handle_add_task(service)
            elif choice == 2:
                handle_view_tasks(service)
            elif choice == 3:
                handle_update_task(service)
            elif choice == 4:
                handle_delete_task(service)
            elif choice == 5:
                handle_toggle_status(service)
            elif choice == 6:
                print("\nGoodbye!")
                break
            else:
                # This shouldn't happen due to validation in get_menu_choice
                display_error("Invalid choice")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nGoodbye!")
            break
        except Exception as e:
            # Catch-all for unexpected errors
            display_error(f"An unexpected error occurred: {e}")
            print("Please try again or contact support if the problem persists.")


if __name__ == "__main__":
    main()
