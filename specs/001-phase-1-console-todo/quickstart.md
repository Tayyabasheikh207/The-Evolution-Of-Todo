# Quickstart Guide: Phase I - Console Todo Application

**Feature**: Phase I Console Todo Application
**Date**: 2026-01-02
**Audience**: End users and developers

## Overview

This quickstart guide walks you through setting up and using the Phase I Todo console application. Phase I is an in-memory Python application with a simple menu-driven interface for managing tasks. All data is stored in memory and will be lost when the application exits.

## Prerequisites

**Required**:
- Python 3.11 or higher installed on your system
- Terminal/Command Prompt access

**To check your Python version**:
```bash
python --version
```

or

```bash
python3 --version
```

**Expected output**: `Python 3.11.0` or higher

## Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd BONSAI
```

### Step 2: Verify Project Structure

Ensure the following structure exists:
```
src/
├── models/
│   └── task.py
├── services/
│   └── task_service.py
├── cli/
│   └── menu.py
└── main.py
```

### Step 3: No Dependencies Required

Phase I has zero external dependencies - it uses Python's standard library only. No `pip install` commands needed!

## Running the Application

### Start the Application

From the project root directory:

**On Windows**:
```bash
python src/main.py
```

**On macOS/Linux**:
```bash
python3 src/main.py
```

### Expected Output

You should see the main menu:

```
=================================
   Todo List - Main Menu
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter your choice (1-6):
```

## Basic Usage

### 1. Add Your First Task

1. Select option `1` (Add Task)
2. Enter a title when prompted: `Buy groceries`
3. Enter a description (or press Enter to skip): `Milk, eggs, bread`
4. You'll see: `✓ Task added successfully (ID: 1)`

**Example**:
```
Enter your choice (1-6): 1

Enter task title: Buy groceries
Enter task description (optional, press Enter to skip): Milk, eggs, bread

✓ Task added successfully (ID: 1)
```

### 2. View Your Tasks

1. Select option `2` (View Tasks)
2. You'll see all your tasks with their IDs, status, and descriptions

**Example**:
```
Enter your choice (1-6): 2

=================================
   Your Tasks
=================================

[1] [Incomplete] Buy groceries
    Description: Milk, eggs, bread

Total: 1 task (0 complete, 1 incomplete)
```

### 3. Mark a Task as Complete

1. Select option `5` (Mark Complete/Incomplete)
2. Enter the task ID: `1`
3. You'll see: `✓ Task 1 marked as Complete`

**Example**:
```
Enter your choice (1-6): 5

Enter task ID: 1

✓ Task 1 marked as Complete
```

### 4. Update a Task

1. Select option `3` (Update Task)
2. Enter the task ID: `1`
3. Enter new title (or press Enter to keep current): `Buy groceries and snacks`
4. Enter new description (or press Enter to keep current): `Milk, eggs, bread, chips`
5. You'll see: `✓ Task 1 updated successfully`

**Example**:
```
Enter your choice (1-6): 3

Enter task ID: 1
Enter new title (press Enter to keep current): Buy groceries and snacks
Enter new description (press Enter to keep current): Milk, eggs, bread, chips

✓ Task 1 updated successfully
```

### 5. Delete a Task

1. Select option `4` (Delete Task)
2. Enter the task ID: `1`
3. You'll see: `✓ Task 1 deleted successfully`

**Example**:
```
Enter your choice (1-6): 4

Enter task ID: 1

✓ Task 1 deleted successfully
```

### 6. Exit the Application

1. Select option `6` (Exit)
2. Application closes (all data is lost - expected behavior for Phase I)

## Complete Usage Example

Here's a complete session demonstrating all features:

```bash
$ python src/main.py

=================================
   Todo List - Main Menu
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter your choice (1-6): 1

Enter task title: Buy groceries
Enter task description (optional, press Enter to skip): Milk, eggs, bread

✓ Task added successfully (ID: 1)

=================================
   Todo List - Main Menu
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter your choice (1-6): 1

Enter task title: Finish report
Enter task description (optional, press Enter to skip): Q4 financial report for management

✓ Task added successfully (ID: 2)

=================================
   Todo List - Main Menu
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter your choice (1-6): 2

=================================
   Your Tasks
=================================

[1] [Incomplete] Buy groceries
    Description: Milk, eggs, bread

[2] [Incomplete] Finish report
    Description: Q4 financial report for management

Total: 2 tasks (0 complete, 2 incomplete)

=================================
   Todo List - Main Menu
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter your choice (1-6): 5

Enter task ID: 1

✓ Task 1 marked as Complete

=================================
   Todo List - Main Menu
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter your choice (1-6): 2

=================================
   Your Tasks
=================================

[1] [Complete] Buy groceries
    Description: Milk, eggs, bread

[2] [Incomplete] Finish report
    Description: Q4 financial report for management

Total: 2 tasks (1 complete, 1 incomplete)

=================================
   Todo List - Main Menu
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter your choice (1-6): 6

Goodbye!
```

## Common Error Messages

### Empty Title Error

**Error**: `✗ Error: Task title cannot be empty`

**Cause**: You pressed Enter without typing a title, or entered only whitespace.

**Solution**: Enter at least one non-whitespace character for the task title.

### Task Not Found Error

**Error**: `✗ Error: Task with ID 5 not found`

**Cause**: You entered an ID that doesn't exist in your task list.

**Solution**: Use option `2` (View Tasks) to see valid task IDs, then try again.

### Invalid ID Format Error

**Error**: `✗ Error: Invalid task ID. Please enter a number.`

**Cause**: You entered a non-numeric value when prompted for a task ID.

**Solution**: Enter a positive integer (e.g., `1`, `2`, `3`).

### Invalid Menu Option Error

**Error**: `✗ Error: Invalid option. Please select a number from the menu.`

**Cause**: You entered a number outside the range 1-6 or a non-numeric value.

**Solution**: Enter a number between 1 and 6 to select a menu option.

## Tips & Best Practices

### Remember Task IDs

- Task IDs are assigned sequentially starting from 1
- Use option `2` (View Tasks) frequently to see task IDs
- IDs are not reused after deletion (e.g., after deleting task 2, the next new task will be ID 4 if 3 tasks were created)

### Use Descriptions Wisely

- Descriptions are optional - skip them for simple tasks
- Add descriptions for tasks that need clarification or have multiple steps
- Maximum 2000 characters for descriptions (titles max 500 characters)

### Empty Task List

- If you haven't added any tasks yet, View Tasks will show: `No tasks found. Your list is empty.`
- This is normal - start by adding your first task with option `1`

### Data Persistence

- **Important**: All data is stored in memory only
- When you exit the application (option `6`), all tasks are lost
- This is expected behavior for Phase I
- Data persistence will be added in Phase II

## Troubleshooting

### Application Won't Start

**Problem**: `ModuleNotFoundError` or `ImportError`

**Solution**: Ensure you're running from the project root directory (`BONSAI/`), not from inside `src/`

**Correct**:
```bash
cd BONSAI
python src/main.py
```

**Incorrect**:
```bash
cd BONSAI/src
python main.py  # This won't work due to import paths
```

### Python Version Too Old

**Problem**: `SyntaxError` or features not supported

**Solution**: Upgrade to Python 3.11+. The application uses modern type hints (e.g., `str | None`) that require Python 3.11 or higher.

### Keyboard Interrupt

**Problem**: Accidentally pressed `Ctrl+C`

**Effect**: Application exits immediately (same as selecting option `6`)

**Solution**: Just restart the application with `python src/main.py`

## Feature Limitations (Phase I)

The following features are **not available** in Phase I:

❌ **No Data Persistence**: Tasks are lost when you exit
❌ **No File Storage**: Cannot save/load tasks from files
❌ **No Multi-User**: Single user only, no authentication
❌ **No Categories or Tags**: Tasks have no categories, tags, or priorities
❌ **No Due Dates**: Cannot set deadlines or reminders
❌ **No Search or Filter**: Must view all tasks, no search functionality
❌ **No Sorting**: Tasks displayed in creation order by ID
❌ **No Web Interface**: Console-only, no web or mobile app
❌ **No API**: No REST API or external integrations

These features will be introduced in Phase II-V per the project roadmap.

## Next Steps

### After Getting Comfortable

1. Try adding multiple tasks and organizing them by completion status
2. Practice updating task titles and descriptions
3. Use the toggle feature to track your progress throughout the day
4. Explore edge cases (empty descriptions, long titles, etc.)

### Learning More

- **Data Model**: See [data-model.md](./data-model.md) for technical details on how tasks are stored
- **Architecture**: See [plan.md](./plan.md) for the technical implementation plan
- **Specification**: See [spec.md](./spec.md) for complete feature requirements

### Providing Feedback

Found a bug or have a suggestion? Contact the development team or open an issue in the project repository.

## Quick Reference

| Operation | Menu Option | What You Need |
|-----------|------------|---------------|
| Add Task | `1` | Title (required), Description (optional) |
| View Tasks | `2` | Nothing |
| Update Task | `3` | Task ID, New Title/Description (optional) |
| Delete Task | `4` | Task ID |
| Toggle Status | `5` | Task ID |
| Exit | `6` | Nothing |

**Task ID**: A number shown in brackets when viewing tasks (e.g., `[1]`, `[2]`, `[3]`)

**Status**: Either `[Complete]` or `[Incomplete]`

---

**Phase I Version**: 1.0
**Last Updated**: 2026-01-02
**For Technical Details**: See [plan.md](./plan.md) and [data-model.md](./data-model.md)
