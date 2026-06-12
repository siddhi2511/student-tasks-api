from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="Student Tasks API",
    description="A simple homework API for tracking student tasks.",
    version="1.0.0",
)


# A task can only have one of these two statuses.
TaskStatus = Literal["pending", "completed"]


class TaskCreate(BaseModel):
    student_name: str
    title: str
    subject: str
    due_date: str
    status: TaskStatus = "pending"


class TaskUpdate(BaseModel):
    student_name: str | None = None
    title: str | None = None
    subject: str | None = None
    due_date: str | None = None
    status: TaskStatus | None = None


class Task(TaskCreate):
    id: int


# This list is our simple temporary storage.
# It resets every time the server restarts.
tasks: list[Task] = [
    Task(
        id=1,
        student_name="Aarav",
        title="Complete algebra worksheet",
        subject="Mathematics",
        due_date="2026-06-20",
        status="pending",
    ),
    Task(
        id=2,
        student_name="Ananya",
        title="Read chapter 5",
        subject="English",
        due_date="2026-06-18",
        status="completed",
    ),
]

next_task_id = 3


def find_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Student Tasks API",
        "docs": "/docs",
    }


@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    return find_task(task_id)


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate):
    global next_task_id

    task = Task(
        id=next_task_id,
        student_name=task_data.student_name,
        title=task_data.title,
        subject=task_data.subject,
        due_date=task_data.due_date,
        status=task_data.status,
    )

    tasks.append(task)
    next_task_id += 1

    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate):
    task = find_task(task_id)

    if task_data.student_name is not None:
        task.student_name = task_data.student_name

    if task_data.title is not None:
        task.title = task_data.title

    if task_data.subject is not None:
        task.subject = task_data.subject

    if task_data.due_date is not None:
        task.due_date = task_data.due_date

    if task_data.status is not None:
        task.status = task_data.status

    return task


@app.patch("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int):
    task = find_task(task_id)
    task.status = "completed"

    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = find_task(task_id)
    tasks.remove(task)

    return {
        "message": "Task deleted successfully",
        "task": task,
    }
