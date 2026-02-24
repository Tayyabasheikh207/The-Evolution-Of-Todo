# Quickstart Guide: Phase II Todo Web Application

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL-compatible database (Neon Serverless PostgreSQL)
- Git
- Package manager (pip for Python, npm/yarn for Node.js)

## Environment Setup

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database connection details and auth secrets
   ```

5. Run database migrations:
   ```bash
   python -m alembic upgrade head
   ```

6. Start the backend server:
   ```bash
   uvicorn src.api.main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or yarn install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your backend API URL
   ```

4. Start the development server:
   ```bash
   npm run dev
   # or yarn dev
   ```

## Configuration

### Backend Configuration

The backend uses a settings module with the following key configurations:
- Database URL (PostgreSQL connection string)
- Secret keys for authentication
- CORS settings for frontend integration
- Logging configuration

### Frontend Configuration

The frontend is configured with:
- API base URL for backend communication
- Authentication settings for Better Auth
- Environment-specific configurations

## Running the Application

1. Start the backend server (port 8000 by default)
2. Start the frontend server (port 3000 by default)
3. Access the application at http://localhost:3000
4. Sign up for a new account or sign in if you have one

## Development Workflow

### Backend Development
- API endpoints are defined in `src/api/routes/`
- Business logic is implemented in `src/services/`
- Data models are defined in `src/models/`
- Use pytest for testing: `pytest`

### Frontend Development
- Pages are organized in the `src/app/` directory using Next.js App Router
- Components are in `src/components/`
- API calls are managed in `src/services/api.ts`
- Use Jest and React Testing Library for testing

## Database Migrations

Run migrations with Alembic:
```bash
# Create a new migration
alembic revision --autogenerate -m "Migration description"

# Apply migrations
alembic upgrade head
```

## Testing

### Backend Tests
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src
```

### Frontend Tests
```bash
# Run all tests
npm run test

# Run tests in watch mode
npm run test:watch
```

## API Documentation

The API is documented with Swagger/OpenAPI. Access the documentation at:
- http://localhost:8000/docs (Interactive API docs)
- http://localhost:8000/redoc (Alternative API docs)