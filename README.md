# Evolution of Todo - Phase I: Console Application

A simple in-memory Python console application for managing todo tasks with basic CRUD operations.

## Features

- ✅ Add tasks with title and optional description
- ✅ View all tasks with status indicators
- ✅ Mark tasks as complete or incomplete
- ✅ Update task details (title and description)
- ✅ Delete tasks
- ✅ Menu-driven command-line interface

## Requirements

- Python 3.11 or higher
- No external dependencies (standard library only)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd BONSAI
```

2. Verify Python version:
```bash
python --version  # Should be 3.11 or higher
```

## Usage

Run the application from the project root:

```bash
python src/main.py
```

### Menu Options

1. **Add Task** - Create a new task with title and optional description
2. **View Tasks** - Display all tasks with their status
3. **Update Task** - Modify an existing task's title or description
4. **Delete Task** - Remove a task from the list
5. **Mark Complete/Incomplete** - Toggle task completion status
6. **Exit** - Close the application

### Example Session

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

Enter your choice (1-6): 1

Enter task title: Buy groceries
Enter task description (optional, press Enter to skip): Milk, eggs, bread

✓ Task added successfully (ID: 1)
```

## Phase I Constraints

- **In-memory storage only** - Tasks are lost when application exits
- **Single user** - No authentication or multi-user support
- **Console interface only** - No web or API access
- **No persistence** - Data does not survive application restart

These limitations are by design for Phase I. Future phases will add:
- Phase II: Database persistence, cloud deployment, authentication
- Phase III: Real-time collaboration, WebSocket support
- Phase IV: Microservices architecture, event-driven patterns
- Phase V: AI-powered features, advanced analytics

## Project Structure

```
BONSAI/
├── src/
│   ├── models/
│   │   └── task.py          # Task dataclass and TaskStatus enum
│   ├── services/
│   │   └── task_service.py  # Business logic and in-memory storage
│   ├── cli/
│   │   └── menu.py          # CLI interface and user interaction
│   └── main.py              # Application entry point
├── tests/                   # Test directory (for future use)
├── specs/                   # Feature specifications and design docs
├── requirements.txt         # Dependencies (empty for Phase I)
└── README.md               # This file
```

## Development

### Architecture

Phase I follows clean architecture with three layers:

1. **Data Layer** (`src/models/`) - Task dataclass and enums
2. **Service Layer** (`src/services/`) - Business logic and storage
3. **Presentation Layer** (`src/cli/`) - User interface and input handling

### Design Documents

See `specs/001-phase-1-console-todo/` for:
- `spec.md` - Feature requirements and user stories
- `plan.md` - Technical implementation plan
- `data-model.md` - Entity definitions and validation rules
- `tasks.md` - Task breakdown for implementation

## License

[Your license here]

## Contributing

[Your contributing guidelines here]
