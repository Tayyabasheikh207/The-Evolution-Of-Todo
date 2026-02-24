# Data Model: Phase II Todo Web Application

## User Entity

**Description**: Represents a registered user with authentication credentials and associated todos

**Fields**:
- `id` (UUID/String): Unique identifier for the user (Primary Key)
- `email` (String): User's email address (Unique, Required, Validated)
- `password_hash` (String): Hashed password for authentication (Required, Secure)
- `created_at` (DateTime): Timestamp of user account creation (Auto-generated)
- `updated_at` (DateTime): Timestamp of last update (Auto-generated)

**Relationships**:
- One-to-Many: User has many Todos (via foreign key in Todo entity)
- Todo.user_id references User.id

**Validation Rules**:
- Email must be a valid email format
- Email must be unique across all users
- Password must meet security requirements (handled by Better Auth)
- All required fields must be present

## Todo Entity

**Description**: Represents a task item owned by a specific user

**Fields**:
- `id` (UUID/String): Unique identifier for the todo (Primary Key)
- `content` (String): The todo task description (Required, Max length: 500 characters)
- `completed` (Boolean): Status indicating if the todo is completed (Default: False)
- `user_id` (UUID/String): Reference to the owning user (Foreign Key to User.id, Required)
- `created_at` (DateTime): Timestamp of todo creation (Auto-generated)
- `updated_at` (DateTime): Timestamp of last update (Auto-generated)

**Relationships**:
- Many-to-One: Todo belongs to one User (via user_id foreign key)
- User.id references Todo.user_id

**Validation Rules**:
- Content must be provided and not empty
- Content must not exceed 500 characters
- user_id must reference an existing user
- Only the owning user can modify/delete the todo

## State Transitions

### Todo State Transitions
- **Active** → **Completed**: When user marks todo as complete
- **Completed** → **Active**: When user marks todo as incomplete

### User State Considerations
- User account can be created (sign-up)
- User session can be started (sign-in)
- User session can be ended (sign-out)

## Constraints

### Data Integrity Constraints
- Foreign key constraint: Todo.user_id must reference existing User.id
- Unique constraint: User.email must be unique
- Not-null constraints: Required fields cannot be null

### Business Logic Constraints
- Users can only access/modify their own todos
- Todos must have valid content (non-empty, within character limit)
- Todos must be associated with a valid user

## Indexes

### Recommended Indexes
- User.email: For efficient email lookups during authentication
- Todo.user_id: For efficient retrieval of user's todos
- Todo.created_at: For chronological ordering of todos
- Todo.completed: For filtering completed vs active todos