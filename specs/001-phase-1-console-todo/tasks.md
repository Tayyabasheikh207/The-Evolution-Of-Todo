# Tasks: Phase I - Console Todo Application

**Input**: Design documents from `/specs/001-phase-1-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md

**Tests**: Tests are NOT requested for Phase I per specification. Focus is on rapid MVP delivery.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root (Phase I structure per plan.md)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure (src/, src/models/, src/services/, src/cli/, tests/)
- [x] T002 Create empty __init__.py files in src/, src/models/, src/services/, src/cli/
- [x] T003 Create requirements.txt with no dependencies (comment: "Python 3.11+ standard library only")
- [x] T004 Create README.md with project description and quick start instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 [P] Create TaskStatus enum in src/models/task.py (INCOMPLETE, COMPLETE values)
- [x] T006 [P] Create Task dataclass in src/models/task.py with fields: id, title, description, status
- [x] T007 [P] Create custom exception classes in src/services/task_service.py (TaskNotFoundError, InvalidInputError)
- [x] T008 Initialize TaskService class in src/services/task_service.py with empty __init__ (dict storage, ID counter)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP Component 1/2

**Goal**: Enable users to add tasks with title and optional description

**Independent Test**: Launch app, select "Add Task", enter title and description, verify task added with ID 1 and status Incomplete

### Implementation for User Story 1

- [x] T009 [US1] Implement TaskService.add_task(title, description) method in src/services/task_service.py
- [x] T010 [US1] Add title validation in TaskService.add_task (non-empty, strip whitespace, max 500 chars with truncation)
- [x] T011 [US1] Add description validation in TaskService.add_task (optional, max 2000 chars with truncation)
- [x] T012 [US1] Implement ID generation logic in TaskService.add_task (sequential counter starting from 1)
- [x] T013 [US1] Store new task in dict with auto-generated ID in TaskService.add_task
- [x] T014 [US1] Create handle_add_task function in src/cli/menu.py (prompt for title and description)
- [x] T015 [US1] Add input validation in handle_add_task (catch empty title, display error "Task title cannot be empty")
- [x] T016 [US1] Display success message in handle_add_task ("✓ Task added successfully (ID: {id})")
- [x] T017 [US1] Add error handling in handle_add_task (catch InvalidInputError, display user-friendly message)

**Checkpoint**: At this point, users can add tasks. Combined with US2 (View), this forms the MVP.

---

## Phase 4: User Story 2 - View Task List (Priority: P1) 🎯 MVP Component 2/2

**Goal**: Display all tasks with ID, title, status, and description

**Independent Test**: Add 3 tasks, select "View Tasks", verify all tasks displayed with correct format and status indicators

### Implementation for User Story 2

- [x] T018 [US2] Implement TaskService.get_all_tasks() method in src/services/task_service.py (return list of all tasks)
- [x] T019 [US2] Create handle_view_tasks function in src/cli/menu.py
- [x] T020 [US2] Implement empty list handling in handle_view_tasks (display "No tasks found. Your list is empty.")
- [x] T021 [US2] Format task display in handle_view_tasks (show [ID] [Status] Title, Description on separate line)
- [x] T022 [US2] Add visual status indicators in handle_view_tasks ([Complete] vs [Incomplete])
- [x] T023 [US2] Add task count summary in handle_view_tasks ("Total: X tasks (Y complete, Z incomplete)")
- [x] T024 [US2] Ensure unicode support in handle_view_tasks (display emojis and special characters correctly)

**Checkpoint**: MVP COMPLETE - Users can add and view tasks (US1 + US2)

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Toggle task status between Complete and Incomplete

**Independent Test**: Add task, mark complete, view to verify status changed, mark incomplete again, verify toggle works

### Implementation for User Story 3

- [x] T025 [US3] Implement TaskService.get_task_by_id(task_id) method in src/services/task_service.py (return task or raise TaskNotFoundError)
- [x] T026 [US3] Implement TaskService.toggle_status(task_id) method in src/services/task_service.py
- [x] T027 [US3] Add status toggle logic in TaskService.toggle_status (INCOMPLETE → COMPLETE, COMPLETE → INCOMPLETE)
- [x] T028 [US3] Create handle_toggle_status function in src/cli/menu.py
- [x] T029 [US3] Add ID input validation in handle_toggle_status (integer check, display "Invalid task ID. Please enter a number.")
- [x] T030 [US3] Handle TaskNotFoundError in handle_toggle_status (display "Error: Task with ID {id} not found")
- [x] T031 [US3] Display success message in handle_toggle_status ("✓ Task {id} marked as {Complete/Incomplete}")

**Checkpoint**: Core productivity feature complete - users can track task completion

---

## Phase 6: User Story 4 - Update Task Details (Priority: P3)

**Goal**: Modify task title and/or description

**Independent Test**: Add task, update title only, verify change; update description only, verify change; attempt empty title, verify error

### Implementation for User Story 4

- [x] T032 [US4] Implement TaskService.update_task(task_id, title, description) method in src/services/task_service.py
- [x] T033 [US4] Add optional field handling in TaskService.update_task (None = no change, string = update)
- [x] T034 [US4] Add title validation in TaskService.update_task (if provided, must be non-empty)
- [x] T035 [US4] Add description validation in TaskService.update_task (max 2000 chars with truncation)
- [x] T036 [US4] Create handle_update_task function in src/cli/menu.py
- [x] T037 [US4] Prompt for task ID in handle_update_task
- [x] T038 [US4] Prompt for new title in handle_update_task (press Enter to keep current)
- [x] T039 [US4] Prompt for new description in handle_update_task (press Enter to keep current)
- [x] T040 [US4] Handle TaskNotFoundError in handle_update_task (display "Error: Task with ID {id} not found")
- [x] T041 [US4] Handle empty title error in handle_update_task (display "Error: Task title cannot be empty")
- [x] T042 [US4] Display success message in handle_update_task ("✓ Task {id} updated successfully")

**Checkpoint**: Task editing complete - users have flexibility to refine task details

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Remove tasks from the list

**Independent Test**: Add 4 tasks, delete task with ID 2, view list to verify 3 tasks remain and deleted task is gone

### Implementation for User Story 5

- [x] T043 [US5] Implement TaskService.delete_task(task_id) method in src/services/task_service.py
- [x] T044 [US5] Remove task from storage dict in TaskService.delete_task (raise TaskNotFoundError if not found)
- [x] T045 [US5] Create handle_delete_task function in src/cli/menu.py
- [x] T046 [US5] Prompt for task ID in handle_delete_task with validation
- [x] T047 [US5] Handle TaskNotFoundError in handle_delete_task (display "Error: Task with ID {id} not found")
- [x] T048 [US5] Display success message in handle_delete_task ("✓ Task {id} deleted successfully")

**Checkpoint**: All CRUD operations complete - full task management capability

---

## Phase 8: Menu System & Main Loop (Cross-Cutting)

**Purpose**: Tie all user stories together with menu-driven interface

- [x] T049 Create display_menu function in src/cli/menu.py (show 6 options: Add, View, Update, Delete, Toggle, Exit)
- [x] T050 Create get_menu_choice function in src/cli/menu.py (get user input, validate 1-6 range)
- [x] T051 Handle invalid menu option in get_menu_choice (display "Invalid option. Please select a number from the menu.")
- [x] T052 Create display_error function in src/cli/menu.py (format: "✗ Error: {message}")
- [x] T053 Create main function in src/main.py (initialize TaskService, run infinite loop)
- [x] T054 Implement menu dispatch logic in src/main.py (choice 1→add, 2→view, 3→update, 4→delete, 5→toggle, 6→exit)
- [x] T055 Add graceful exit in src/main.py (choice 6 breaks loop, display "Goodbye!")
- [x] T056 Add catch-all exception handler in src/main.py (unexpected errors display friendly message)
- [x] T057 Add if __name__ == "__main__" guard in src/main.py to call main()

**Checkpoint**: Complete application ready for end-to-end testing

---

## Phase 9: Polish & Validation

**Purpose**: Final refinements and validation

- [x] T058 [P] Verify all error messages match specification wording exactly
- [x] T059 [P] Test unicode support (add tasks with emojis and special characters)
- [x] T060 [P] Test title truncation (add task with 501+ character title, verify "..." truncation)
- [x] T061 [P] Test description truncation (add task with 2001+ character description, verify "..." truncation)
- [x] T062 [P] Verify empty task list message displays correctly on startup
- [x] T063 [P] Test all acceptance scenarios from spec.md for US1 (4 scenarios)
- [x] T064 [P] Test all acceptance scenarios from spec.md for US2 (4 scenarios)
- [x] T065 [P] Test all acceptance scenarios from spec.md for US3 (4 scenarios)
- [x] T066 [P] Test all acceptance scenarios from spec.md for US4 (4 scenarios)
- [x] T067 [P] Test all acceptance scenarios from spec.md for US5 (4 scenarios)
- [x] T068 [P] Verify performance: add 1000 tasks, verify operations remain fast (<500ms)
- [x] T069 Update README.md with complete usage instructions and examples

**Checkpoint**: Phase I complete and validated against all acceptance criteria

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - US1 (Add Task) - Can start after Foundational
  - US2 (View Tasks) - Can start after Foundational (independent of US1, but MVP requires both)
  - US3 (Toggle Status) - Depends on US2 (requires get_task_by_id from US3's T025)
  - US4 (Update Task) - Depends on US3 (requires get_task_by_id)
  - US5 (Delete Task) - Can start after Foundational (independent, but requires get_task_by_id pattern from US3)
- **Menu System (Phase 8)**: Depends on US1 and US2 minimum (MVP); full menu requires US1-US5
- **Polish (Phase 9)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Independent of US1, but both needed for MVP
- **User Story 3 (P2)**: Requires T025 (get_task_by_id) which can be implemented in US3's phase
- **User Story 4 (P3)**: Uses get_task_by_id pattern established in US3
- **User Story 5 (P3)**: Can reuse get_task_by_id pattern from US3

### Within Each User Story

- **Foundational Phase**: All [P] tasks (T005-T007) can run in parallel
- **US1**: T009-T013 (service layer) before T014-T017 (CLI layer)
- **US2**: T018 (service) before T019-T024 (CLI)
- **US3**: T025-T027 (service) before T028-T031 (CLI)
- **US4**: T032-T035 (service) before T036-T042 (CLI)
- **US5**: T043-T044 (service) before T045-T048 (CLI)
- **Menu System**: All tasks sequential (T049-T057)
- **Polish**: All [P] tasks (T058-T069) can run in parallel

### Parallel Opportunities

- **Setup Phase**: T001-T004 are sequential (directory structure first)
- **Foundational Phase**: T005, T006, T007 can run in parallel (different concerns)
- **User Story Phases**: Service layer tasks within each story could be parallel if split by concern
- **Polish Phase**: T058-T069 are all independent validation tasks - full parallelization possible

---

## Parallel Example: Foundational Phase

```bash
# Launch all foundational tasks together:
Task: "Create TaskStatus enum in src/models/task.py"
Task: "Create Task dataclass in src/models/task.py"
Task: "Create custom exception classes in src/services/task_service.py"

# All three touch different aspects and can be implemented simultaneously
```

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T008)
3. Complete Phase 3: User Story 1 - Add Task (T009-T017)
4. Complete Phase 4: User Story 2 - View Tasks (T018-T024)
5. Complete Phase 8: Menu System (T049-T057) - Simplified version with only options 1, 2, 6
6. **STOP and VALIDATE**: Test MVP (add tasks, view tasks, exit)
7. Deploy/demo if ready

### Incremental Delivery (All User Stories)

1. Complete Setup + Foundational (T001-T008) → Foundation ready
2. Add User Story 1 + User Story 2 + Basic Menu → Test independently → MVP deployed
3. Add User Story 3 + Update Menu → Test independently → Deploy v1.1 (task completion tracking)
4. Add User Story 4 + Update Menu → Test independently → Deploy v1.2 (task editing)
5. Add User Story 5 + Update Menu → Test independently → Deploy v1.3 (full CRUD)
6. Add Polish + Validation → Test all scenarios → Deploy v1.0 final
7. Each increment adds value without breaking previous features

### Full Parallel Team Strategy

With multiple developers (or parallel agent execution):

1. **Team completes Setup + Foundational together** (T001-T008)
2. **Once Foundational is done**:
   - Developer A: User Story 1 (T009-T017)
   - Developer B: User Story 2 (T018-T024)
   - Developer C: User Story 3 (T025-T031) - starts after US2's get_task_by_id pattern
3. **After US1-US3 complete**:
   - Developer A: User Story 4 (T032-T042)
   - Developer B: User Story 5 (T043-T048)
   - Developer C: Menu System (T049-T057)
4. **Final phase**:
   - All developers: Polish tasks in parallel (T058-T069)

---

## Task Summary

**Total Tasks**: 69

**Breakdown by Phase**:
- Phase 1 (Setup): 4 tasks
- Phase 2 (Foundational): 4 tasks (3 parallelizable)
- Phase 3 (US1 - Add Task): 9 tasks
- Phase 4 (US2 - View Tasks): 7 tasks
- Phase 5 (US3 - Toggle Status): 7 tasks
- Phase 6 (US4 - Update Task): 11 tasks
- Phase 7 (US5 - Delete Task): 6 tasks
- Phase 8 (Menu System): 9 tasks
- Phase 9 (Polish): 12 tasks (all parallelizable)

**Parallelizable Tasks**: 15 tasks (marked with [P])

**MVP Scope** (Minimum Viable Product):
- Phase 1 (T001-T004): Setup
- Phase 2 (T005-T008): Foundation
- Phase 3 (T009-T017): User Story 1
- Phase 4 (T018-T024): User Story 2
- Phase 8 (T049-T057): Basic Menu System
- **Total MVP Tasks**: 33 tasks (48% of total)

**Independent Test Criteria**:
- US1: Add task, verify ID assigned and status is Incomplete
- US2: View tasks, verify all tasks displayed with correct formatting
- US3: Toggle task status, verify status changes between Complete/Incomplete
- US4: Update task, verify title and/or description changed
- US5: Delete task, verify task removed from list

---

## Notes

- No [P] markers on Setup (T001-T004) - must be sequential (directory structure first)
- Foundational phase T005-T007 can be parallel (different files and concerns)
- Each user story phase is independently completable and testable
- Service layer tasks precede CLI layer tasks within each story (dependency on business logic)
- Menu system ties everything together - can start with MVP subset (US1, US2, Exit)
- Polish phase is fully parallelizable (all validation tasks are independent)
- Tests are NOT included per specification (no TDD requested for Phase I)
- Commit after each completed user story phase for incremental delivery
- Stop at any checkpoint to validate story independently before proceeding
