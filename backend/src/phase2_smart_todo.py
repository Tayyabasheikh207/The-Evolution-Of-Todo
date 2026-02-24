from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session, select

# 1. Database Configuration (Using SQLite for no-password setup)
sqlite_url = "sqlite:///./robotic_todo.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

# 2. Physical AI Task Model
class RoboticTask(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    task_name: str
    robot_action: str  # Example: "Pick and Place", "Wave", "Walk"
    joint_angle: int = 0  # Physical AI concept: Servo motor angle
    is_completed: bool = False

app = FastAPI(title="Humanoid Todo - Phase 2")

# Create tables on startup
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to Humanoid AI Todo Phase 2"}

@app.post("/tasks/")
def create_task(task: RoboticTask):
    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

@app.get("/tasks/")
def get_tasks():
    with Session(engine) as session:
        tasks = session.exec(select(RoboticTask)).all()
        return tasks