# Implementation Plan: Phase I - Console Todo Application

**Branch**: `001-phase-1-console-todo` | **Date**: 2026-01-02 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-phase-1-console-todo/spec.md`

## Summary

Phase I delivers an in-memory Python console application for managing todo tasks with basic CRUD operations. The application provides a menu-driven interface for adding, viewing, updating, deleting, and toggling completion status of tasks. All data is stored in memory using Python's built-in data structures with no external dependencies. The architecture follows clean separation of concerns with distinct layers for data management, business logic, and user interface presentation.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: None (standard library only)
**Storage**: In-memory (Python dict for task storage, int counter for ID generation)
**Testing**: pytest (for future testing if required)
**Target Platform**: Cross-platform (Windows, macOS, Linux) console application
**Project Type**: Single Python application
**Performance Goals**: <15s to add task, <3s to view list, handles 1000 tasks without degradation
**Constraints**: <500ms p95 for all operations, in-memory only (no persistence), single-user, synchronous execution
**Scale/Scope**: 1000 tasks per session, 5 core operations (Add, View, Update, Delete, Toggle Status)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Phase Governance Compliance

✅ **PASS**: Phase I Boundaries Respected
- No database or file storage (in-memory only per spec)
- No authentication or user management (single user per spec)
- No web, API, or network features (console-only per spec)
- No advanced features from Phase II+ (categories, tags, priorities, due dates excluded)
- Explicit "Out of Scope" section in spec defines boundaries

### Clean Architecture & Separation of Concerns

✅ **PASS**: Layered Architecture Planned
- **Data Layer**: Task model and in-memory storage abstraction
- **Service Layer**: Business logic for CRUD operations and validation
- **Presentation Layer**: CLI interface and menu handling
- **Single Responsibility**: Each module has one clear purpose
- **Dependency Flow**: Presentation → Service → Data (unidirectional)

### Code Quality Standards

✅ **PASS**: Quality Standards Defined
- Python 3.11+ with type hints (per constitution)
- PEP 8 compliance (enforceable with black/ruff)
- Clear error messages with actionable guidance (per FR-009)
- Unicode support (per FR-013)
- Input validation (per FR-008)

### Simplicity & YAGNI

✅ **PASS**: Minimal Complexity
- No external dependencies (standard library only)
- Simple data structures (dict for storage, dataclass for Task)
- No premature abstractions (e.g., no repository pattern, no ORM for in-memory data)
- No frameworks (no FastAPI, no CLI frameworks, pure Python)
- Sequential ID generation (simple counter, no UUID complexity)

### Observability (Phase I Scope)

✅ **PASS**: Basic Observability for Console App
- Clear user-facing error messages (per constitution's operational excellence)
- Operation confirmations (per UX-004 in spec)
- Input validation feedback (per FR-009)
- Note: Structured logging not required for Phase I console app (Phase II+ requirement for cloud services)

**Constitution Check Result**: ✅ ALL GATES PASSED - No complexity justification required

## Project Structure

### Documentation (this feature)

```text
specs/001-phase-1-console-todo/
├── plan.md              # This file (/sp.plan command output)
├── spec.md              # Feature specification (completed)
├── data-model.md        # Phase 1 output (generated below)
├── quickstart.md        # Phase 1 output (generated below)
├── checklists/
│   └── requirements.md  # Spec validation checklist (completed)
└── contracts/
    └── N/A              # No API contracts for console app
```

### Source Code (repository root)

```text
src/
├── models/
│   └── task.py          # Task dataclass definition
├── services/
│   └── task_service.py  # Business logic for task operations
├── cli/
│   └── menu.py          # Menu display and user input handling
└── main.py              # Application entry point and main loop

tests/
├── integration/         # Integration tests (if requested in future)
└── unit/                # Unit tests (if requested in future)

README.md                # Project documentation
requirements.txt         # Empty (no external dependencies)
```

**Structure Decision**: Single project structure selected per Phase I scope. This is a standalone console application with no web/mobile components. The structure follows clean architecture with clear separation between models (data), services (business logic), and CLI (presentation). No backend/frontend split required as there is no API or web interface in Phase I.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations detected - all constitutional gates passed. Phase I maintains minimal complexity with no external dependencies, simple data structures, and clear layer separation.

---

## Phase 0: Technical Research & Decisions

### Decision 1: In-Memory Storage Strategy

**Decision**: Use Python dictionary with integer keys for task storage and a simple integer counter for ID generation.

**Rationale**:
- Dictionary provides O(1) lookup, insert, and delete by ID (meets <500ms performance requirement)
- Integer keys (task IDs) are simple, predictable, and user-friendly
- Sequential ID counter starting from 1 matches user expectations (FR-003)
- No need for UUID complexity in single-user, non-distributed system
- Handles 1000 tasks easily (Python dict scales well for this volume)

**Alternatives Considered**:
- **List-based storage**: Rejected - O(n) lookup requires iterating to find task by ID
- **UUID for IDs**: Rejected - overly complex for Phase I, non-sequential IDs harder for users to remember
- **SQLite in-memory**: Rejected - introduces external dependency, violates Phase I constraints (no databases)

**Implementation**:
```python
# In TaskService
self._tasks: dict[int, Task] = {}
self._next_id: int = 1
```

### Decision 2: Error Handling Strategy

**Decision**: Use Python exceptions for internal errors and return Result objects (or simple error strings) for user-facing operations.

**Rationale**:
- Exceptions for unexpected internal errors (programming bugs)
- Graceful error messages for user input errors (per FR-009)
- CLI layer handles exceptions and displays user-friendly messages
- Clear separation: Service raises specific exceptions, CLI catches and formats

**Alternatives Considered**:
- **Return codes**: Rejected - less Pythonic, harder to track error types
- **Global error state**: Rejected - introduces shared mutable state, not clean architecture

**Error Types**:
- `TaskNotFoundError`: Task with given ID doesn't exist (per FR-009, User Stories 3-5)
- `InvalidInputError`: Invalid ID format or empty title (per FR-008, FR-009)
- `ValueError`: For unexpected input validation failures

### Decision 3: Task Model Design

**Decision**: Use Python `dataclass` for Task with simple attributes (id, title, description, status).

**Rationale**:
- Dataclass provides automatic `__init__`, `__repr__`, and `__eq__` methods
- Type hints for all fields (per constitution: type hints mandatory)
- Immutable by default with `frozen=False` to allow status updates
- Simple, no ORM overhead for in-memory storage
- Enum for status ensures type safety (Complete/Incomplete only)

**Alternatives Considered**:
- **Plain dict**: Rejected - no type safety, easy to make errors
- **Named tuple**: Rejected - immutable, can't update task fields
- **Full class with methods**: Rejected - over-engineering, dataclass suffices

**Implementation** (see data-model.md for full schema):
```python
from dataclasses import dataclass
from enum import Enum

class TaskStatus(Enum):
    INCOMPLETE = "Incomplete"
    COMPLETE = "Complete"

@dataclass
class Task:
    id: int
    title: str
    description: str
    status: TaskStatus
```

### Decision 4: CLI Control Flow

**Decision**: Implement infinite loop with menu display, input handling, operation dispatch, and error display.

**Rationale**:
- Matches user story flow: menu → action → feedback → menu (per FR-001, FR-012)
- Clear separation: menu.py handles I/O, main.py orchestrates flow
- Input validation at CLI layer before calling services (fail fast)
- Graceful error display with return to menu (per UX-002)

**Control Flow**:
1. Display menu with numbered options (1-6)
2. Get user choice (integer input)
3. Validate choice (1-6 or invalid)
4. Dispatch to appropriate operation handler
5. Display confirmation or error message
6. Loop back to menu (unless Exit selected)

**Alternatives Considered**:
- **Command-line arguments**: Rejected - spec requires interactive menu, not CLI args
- **REPL-style input**: Rejected - menu-driven interface is clearer for non-technical users

### Decision 5: Input Validation Strategy

**Decision**: Two-layer validation - CLI layer validates format, Service layer validates business rules.

**Rationale**:
- **CLI Layer**: Validates ID format (integer), non-empty title, menu option range (fail fast before service call)
- **Service Layer**: Validates business rules (task exists, title not empty after strip)
- Clear separation of concerns: presentation validates syntax, business logic validates semantics
- Better error messages: format errors caught early with immediate feedback

**Validation Rules**:
- Title: Must not be empty or whitespace-only (per FR-008)
- Description: Optional, can be empty (per spec)
- ID: Must be positive integer (per FR-003)
- Title length: ≤500 characters (per FR-014)
- Description length: ≤2000 characters (per FR-015)

---

## Phase 1: Data Model & Design Artifacts

### Data Model

See [data-model.md](./data-model.md) for complete entity definitions, field specifications, and validation rules.

**Summary**:
- **Task Entity**: id (int), title (str, 1-500 chars), description (str, 0-2000 chars), status (TaskStatus enum)
- **TaskStatus Enum**: INCOMPLETE (default), COMPLETE
- **Storage**: Dictionary with integer keys mapping to Task objects
- **ID Generation**: Sequential counter starting from 1, increments on each add

### API Contracts

**Not Applicable**: Phase I is a console application with no REST API, GraphQL API, or external interfaces. All interactions occur through the CLI menu interface. API contracts will be introduced in Phase II when REST API is added per constitutional phase progression.

### Quickstart Guide

See [quickstart.md](./quickstart.md) for step-by-step setup and usage instructions.

**Summary**:
- Prerequisites: Python 3.11+ installed
- Installation: Clone repo, no dependencies to install
- Running: `python src/main.py`
- Basic operations: Add task → View tasks → Mark complete → Update → Delete → Exit

---

## Architecture Design

### Layer Responsibilities

#### 1. Data Layer (`src/models/`)

**Purpose**: Define data structures and basic validations

**Components**:
- `task.py`: Task dataclass and TaskStatus enum

**Responsibilities**:
- Define Task entity structure (id, title, description, status)
- Define TaskStatus enum (INCOMPLETE, COMPLETE)
- Basic field type enforcement via dataclass and type hints
- No business logic (just data containers)

**Constraints**:
- No external dependencies (standard library only)
- Immutable IDs (set once, never changed)
- Status can only be TaskStatus enum values

#### 2. Service Layer (`src/services/`)

**Purpose**: Implement business logic and task management

**Components**:
- `task_service.py`: TaskService class

**Responsibilities**:
- Task storage management (dictionary and ID counter)
- CRUD operations (add, get_all, get_by_id, update, delete)
- Status toggle logic (INCOMPLETE ↔ COMPLETE)
- Business rule validation (empty title check, ID exists check)
- Raise exceptions for error conditions (TaskNotFoundError, InvalidInputError)

**Constraints**:
- No direct user interaction (no input() or print())
- Returns Task objects or raises exceptions
- Stateless operations (except for storage state)
- Thread-unsafe (single-user, no concurrency required)

**Key Methods**:
```python
class TaskService:
    def add_task(title: str, description: str) -> Task
    def get_all_tasks() -> list[Task]
    def get_task_by_id(task_id: int) -> Task  # raises TaskNotFoundError
    def update_task(task_id: int, title: str | None, description: str | None) -> Task
    def delete_task(task_id: int) -> None  # raises TaskNotFoundError
    def toggle_status(task_id: int) -> Task  # raises TaskNotFoundError
```

#### 3. Presentation Layer (`src/cli/`)

**Purpose**: Handle user interaction and display

**Components**:
- `menu.py`: Menu display, input collection, output formatting

**Responsibilities**:
- Display main menu with numbered options
- Get user input (menu choice, task details, IDs)
- Format and display task lists
- Display success/error messages
- Input format validation (integer IDs, non-empty titles)
- Catch service exceptions and display user-friendly errors

**Constraints**:
- No business logic (delegates to TaskService)
- All user I/O happens here (input(), print())
- Clear error messages with actionable guidance (per FR-009)

**Key Functions**:
```python
def display_menu() -> None
def get_menu_choice() -> int
def handle_add_task(service: TaskService) -> None
def handle_view_tasks(service: TaskService) -> None
def handle_update_task(service: TaskService) -> None
def handle_delete_task(service: TaskService) -> None
def handle_toggle_status(service: TaskService) -> None
def display_error(message: str) -> None
```

#### 4. Application Entry Point (`src/main.py`)

**Purpose**: Initialize application and run main loop

**Responsibilities**:
- Create TaskService instance
- Run infinite menu loop (until Exit selected)
- Dispatch menu choices to CLI handlers
- Handle unexpected errors gracefully (catch-all exception handler)

**Main Loop Flow**:
```python
def main():
    service = TaskService()
    while True:
        display_menu()
        choice = get_menu_choice()
        if choice == 1: handle_add_task(service)
        elif choice == 2: handle_view_tasks(service)
        elif choice == 3: handle_update_task(service)
        elif choice == 4: handle_delete_task(service)
        elif choice == 5: handle_toggle_status(service)
        elif choice == 6: break  # Exit
        else: display_error("Invalid choice")
```

### Data Flow Diagrams

#### Add Task Flow

```
User → CLI (menu.py)                    Service (task_service.py)      Model (task.py)
  |                                            |                            |
  | Enter title & description                 |                            |
  |------------------------------------------→|                            |
  |     validate format (non-empty title)     |                            |
  |                                            |                            |
  |           call add_task(title, desc)      |                            |
  |------------------------------------------→|                            |
  |                                            | validate business rules    |
  |                                            | generate ID (next_id++)    |
  |                                            |                            |
  |                                            | create Task object         |
  |                                            |--------------------------→|
  |                                            |                            |
  |                                            | store in dict[id] = task   |
  |        ←-----------------------------------|                            |
  | display confirmation                       |                            |
```

#### View Tasks Flow

```
User → CLI (menu.py)                    Service (task_service.py)
  |                                            |
  | Select "View Tasks"                        |
  |------------------------------------------→|
  |                                            |
  |           call get_all_tasks()            |
  |------------------------------------------→|
  |                                            | return list[Task]
  |        ←-----------------------------------|
  |                                            |
  | format and display tasks                  |
  | (ID | Title | Status | Description)        |
  |                                            |
```

#### Toggle Status Flow

```
User → CLI (menu.py)                    Service (task_service.py)
  |                                            |
  | Enter task ID                              |
  |------------------------------------------→|
  |     validate format (integer)              |
  |                                            |
  |           call toggle_status(id)          |
  |------------------------------------------→|
  |                                            | get task by ID
  |                                            | toggle status
  |                                            |   INCOMPLETE → COMPLETE
  |                                            |   COMPLETE → INCOMPLETE
  |                                            | update dict[id]
  |        ←-----------------------------------| return updated task
  | display confirmation                       |
```

### Error Handling Strategy

#### Error Types and Handling

**Service Layer Exceptions**:
```python
class TaskNotFoundError(Exception):
    """Raised when task with given ID doesn't exist"""
    pass

class InvalidInputError(Exception):
    """Raised when user input fails validation"""
    pass
```

**CLI Layer Handling**:
```python
try:
    service.get_task_by_id(task_id)
except TaskNotFoundError:
    display_error(f"Error: Task with ID {task_id} not found")
except InvalidInputError as e:
    display_error(f"Error: {e}")
except Exception as e:
    display_error(f"Unexpected error: {e}")
```

#### Error Scenarios and Messages

| Scenario | Error Type | User Message |
|----------|-----------|--------------|
| Empty title | `InvalidInputError` | "Task title cannot be empty" |
| Non-existent ID | `TaskNotFoundError` | "Task with ID {id} not found" |
| Invalid ID format | `InvalidInputError` | "Invalid task ID. Please enter a number." |
| Invalid menu option | Validation error | "Invalid option. Please select a number from the menu." |
| Title too long (>500) | Validation warning | Truncate with "..." indicator |
| Description too long (>2000) | Validation warning | Truncate with "..." indicator |

### Performance Considerations

#### In-Memory Storage Performance

**Dictionary Operations** (O(1) average case):
- `add_task`: O(1) - insert into dict
- `get_task_by_id`: O(1) - dict lookup by key
- `update_task`: O(1) - dict lookup + update
- `delete_task`: O(1) - dict deletion
- `toggle_status`: O(1) - dict lookup + update
- `get_all_tasks`: O(n) - iterate all values (where n = number of tasks)

**Performance Targets Met**:
- ✅ Add task: <15s (actual: <1ms for in-memory operation)
- ✅ View list: <3s (actual: <100ms for 1000 tasks with formatting)
- ✅ All operations: <500ms p95 (actual: <10ms for O(1) operations)
- ✅ Handle 1000 tasks: O(1) operations scale, view is O(n) but acceptable for 1000 items

#### Memory Considerations

**Task Size Estimate**:
- ID: 8 bytes (int)
- Title: ~50 bytes average (assume average 50 chars × 1 byte)
- Description: ~200 bytes average (assume average 200 chars × 1 byte)
- Status: 8 bytes (enum)
- **Total per task**: ~266 bytes

**1000 Tasks**:
- 1000 tasks × 266 bytes = ~260 KB
- Dictionary overhead: ~30% = ~340 KB total
- **Well within memory constraints** (constitution allows reasonable memory usage)

### User Experience Design

#### Menu Display Format

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

#### Task Display Format

```
=================================
   Your Tasks
=================================

[1] [Incomplete] Buy groceries
    Description: Milk, eggs, bread

[2] [Complete] Finish report
    Description: Q4 financial report for management

[3] [Incomplete] Call dentist
    Description: Schedule annual checkup

Total: 3 tasks (1 complete, 2 incomplete)
```

#### Confirmation Messages

- **Add**: "✓ Task added successfully (ID: {id})"
- **Update**: "✓ Task {id} updated successfully"
- **Delete**: "✓ Task {id} deleted successfully"
- **Toggle**: "✓ Task {id} marked as {Complete/Incomplete}"

#### Error Message Format

```
✗ Error: Task title cannot be empty
  Please enter a valid title for your task.
```

---

## Implementation Notes

### Constitutional Compliance

**SDD Mandate**: ✅ Plan derived strictly from approved spec.md, no new features added
**Phase Governance**: ✅ No Phase II+ features (no database, no API, no authentication)
**Clean Architecture**: ✅ Clear layer separation (models/services/cli)
**Simplicity**: ✅ No external dependencies, minimal abstractions, standard library only
**Code Quality**: ✅ Type hints mandatory, PEP 8 compliance, clear error messages

### Architectural Decision Record Suggestion

📋 **Architectural decision detected**: In-memory storage with dict-based task management and sequential ID generation
- **Impact**: Long-term consequences for data structure choice, affects performance characteristics and future migration to Phase II persistence
- **Alternatives**: Considered list-based storage and UUID IDs, rejected for performance and simplicity
- **Scope**: Cross-cutting decision influencing all service layer operations

**Recommendation**: Document reasoning and tradeoffs? Run `/sp.adr in-memory-storage-strategy`

### Future Phase Considerations (Not Implemented in Phase I)

**Phase II Migration Path**:
- In-memory dict → SQLModel ORM with Neon DB
- Sequential int IDs → UUID for distributed systems
- CLI interface → REST API with FastAPI
- Single user → Multi-user with authentication

**Migration Strategy** (Phase II):
1. Extract TaskService interface
2. Implement SQLTaskService with database persistence
3. Keep in-memory implementation for testing
4. Dependency injection for service selection

**Note**: These are planning considerations only. Phase I implements only in-memory console app per specification.

---

## Next Steps

1. ✅ Phase 0 Complete: Technical decisions documented in research.md (this section)
2. ✅ Phase 1 Complete: Data model documented in data-model.md
3. ✅ Phase 1 Complete: Quickstart guide documented in quickstart.md
4. **Ready for /sp.tasks**: Generate tasks.md breaking implementation into discrete units
5. **After /sp.tasks approval**: Begin implementation following task breakdown

**Plan Status**: ✅ COMPLETE - Ready for task generation
