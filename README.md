# Student Tasks API

This is a simple API project made with FastAPI.

It helps students track homework tasks by student name, task title, subject, due date, and status.

This project is beginner-friendly and good for explaining in school because it uses:

- One main Python file
- Simple API routes
- No database
- Easy testing through Swagger UI

## Live Project Links

GitHub repository:

```text
https://github.com/siddhi2511/student-tasks-api
```

Live Render API:

```text
https://student-tasks-api-somj.onrender.com
```

Live Swagger UI:

```text
https://student-tasks-api-somj.onrender.com/docs
```

Use the Swagger UI link if you want to test the API without installing anything.

## What Is An API?

An API is a way for one program to talk to another program.

For example, if a website or app wants to see a student's homework tasks, it can ask this API:

```text
GET /tasks
```

The API then sends back the task data.

## What Problem Does This API Solve?

Students often need to remember:

- What homework they have
- Which subject it belongs to
- When it is due
- Whether it is completed or still pending

This API stores that information as tasks.

## Project Files

| File | Purpose |
| --- | --- |
| `main.py` | The main FastAPI application |
| `requirements.txt` | The Python packages needed to run the project |
| `README.md` | Project explanation and instructions |

## Important Note About Storage

This project uses in-memory storage.

That means the tasks are stored in a Python list while the server is running.

If the server restarts, newly added tasks will disappear. This is normal for this beginner version because we are not using a database.

## Features

- Show all tasks
- Show one task by ID
- Add a new task
- Update a task
- Mark a task as completed
- Delete a task
- Test everything in Swagger UI

## Task Data

Each task has these fields:

| Field | Meaning | Example |
| --- | --- | --- |
| `id` | Unique task number | `1` |
| `student_name` | Name of the student | `"Aarav"` |
| `title` | Task title | `"Complete algebra worksheet"` |
| `subject` | School subject | `"Mathematics"` |
| `due_date` | Due date | `"2026-06-20"` |
| `status` | Task status | `"pending"` |

The `status` can only be:

- `pending`
- `completed`

## API Endpoints

| Method | URL | What It Does |
| --- | --- | --- |
| `GET` | `/` | Shows a welcome message |
| `GET` | `/tasks` | Shows all tasks |
| `GET` | `/tasks/{task_id}` | Shows one task |
| `POST` | `/tasks` | Adds a new task |
| `PUT` | `/tasks/{task_id}` | Updates a task |
| `PATCH` | `/tasks/{task_id}/complete` | Marks a task as completed |
| `DELETE` | `/tasks/{task_id}` | Deletes a task |

## How To Use The Live API From Scratch

This is the easiest way because the API is already deployed online.

### Step 1: Open The Live Swagger UI

Open this link:

```text
https://student-tasks-api-somj.onrender.com/docs
```

Swagger UI is a web page that lets you test the API by clicking buttons.

### Step 2: View All Tasks

1. Find `GET /tasks`.
2. Click it.
3. Click `Try it out`.
4. Click `Execute`.

You should see the sample tasks in the response.

### Step 3: Create A New Task

1. Find `POST /tasks`.
2. Click it.
3. Click `Try it out`.
4. Paste this example into the request body:

```json
{
  "student_name": "Siddhi",
  "title": "Complete API homework",
  "subject": "Computer Science",
  "due_date": "2026-06-30",
  "status": "pending"
}
```

5. Click `Execute`.

The API will return the new task with an `id`.

Example:

```json
{
  "student_name": "Siddhi",
  "title": "Complete API homework",
  "subject": "Computer Science",
  "due_date": "2026-06-30",
  "status": "pending",
  "id": 3
}
```

Remember the `id` because you need it for update, complete, and delete.

### Step 4: Update A Task

1. Find `PUT /tasks/{task_id}`.
2. Click `Try it out`.
3. Enter the task ID, for example `3`.
4. Paste this body:

```json
{
  "title": "Complete and submit API homework",
  "status": "pending"
}
```

5. Click `Execute`.

The task title should be updated.

### Step 5: Mark A Task Completed

1. Find `PATCH /tasks/{task_id}/complete`.
2. Click `Try it out`.
3. Enter the task ID, for example `3`.
4. Click `Execute`.

The task status should change to:

```text
completed
```

### Step 6: Delete A Task

1. Find `DELETE /tasks/{task_id}`.
2. Click `Try it out`.
3. Enter the task ID, for example `3`.
4. Click `Execute`.

You should see:

```text
Task deleted successfully
```

### Step 7: Test A Wrong ID

Try:

```text
GET /tasks/999
```

The API should return `404 Task not found`.

## How To Run This Project

### Step 1: Open The Project Folder

Open a terminal in this folder:

```text
C:\Codex Shit\Hhw_API
```

### Step 2: Install Packages

Run this command:

```bash
pip install -r requirements.txt
```

This installs FastAPI and Uvicorn.

FastAPI creates the API.

Uvicorn runs the API server.

### Step 3: Start The API

Run this command:

```bash
uvicorn main:app --reload
```

If it works, you will see a local server URL like this:

```text
http://127.0.0.1:8000
```

If port `8000` is already busy, run it on another port:

```bash
uvicorn main:app --reload --port 8001
```

### Step 4: Open Swagger UI

Open this URL in your browser:

```text
http://127.0.0.1:8000/docs
```

Swagger UI lets you test the API without Postman or extra tools.

## How To Test The API In Swagger UI

### Create A Task

Use:

```text
POST /tasks
```

Example body:

```json
{
  "student_name": "Rahul",
  "title": "Prepare science notes",
  "subject": "Science",
  "due_date": "2026-06-25",
  "status": "pending"
}
```

### View All Tasks

Use:

```text
GET /tasks
```

### View One Task

Use:

```text
GET /tasks/1
```

### Update A Task

Use:

```text
PUT /tasks/1
```

Example body:

```json
{
  "title": "Complete full algebra worksheet",
  "status": "pending"
}
```

### Mark A Task Completed

Use:

```text
PATCH /tasks/1/complete
```

### Delete A Task

Use:

```text
DELETE /tasks/1
```

### Test An Error

Try opening a task ID that does not exist:

```text
GET /tasks/999
```

You should get a `404` error with this message:

```json
{
  "detail": "Task not found"
}
```

## Easy Explanation For Your Project

You can explain it like this:

> I made a Student Tasks API using FastAPI. It helps store homework tasks for students. Each task has a student name, title, subject, due date, and status. The API has routes to add, view, update, complete, and delete tasks. I used in-memory storage, so the data is stored in a Python list while the server is running. I tested the API using Swagger UI.

## How The Code Works

### `FastAPI`

This creates the API app:

```python
app = FastAPI()
```

### Models

The models describe what task data should look like.

For example, a new task needs:

- `student_name`
- `title`
- `subject`
- `due_date`
- `status`

### Task List

The tasks are stored in a Python list:

```python
tasks = []
```

In this project, the list already has sample tasks.

### Routes

Routes are the URLs of the API.

For example:

```python
@app.get("/tasks")
```

This route shows all tasks.

## Upload To GitHub Using The Website

This is the easiest method.

1. Go to GitHub.
2. Create a new repository.
3. Give it a name like `student-tasks-api`.
4. Do not add another README because this project already has one.
5. Upload these files:
   - `main.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
6. Click commit changes.

## Upload To GitHub Using Git Commands

Open the terminal in the project folder and run these commands.

First, create a local Git repository:

```bash
git init
```

Add the files:

```bash
git add main.py requirements.txt README.md .gitignore
```

Create your first commit:

```bash
git commit -m "Add student tasks API"
```

Connect your GitHub repository:

```bash
git remote add origin https://github.com/YOUR_USERNAME/student-tasks-api.git
```

Rename the branch to `main`:

```bash
git branch -M main
```

Push the code:

```bash
git push -u origin main
```

Replace `YOUR_USERNAME` with your real GitHub username.

## Deploy On Render

After uploading the project to GitHub, you can deploy it on Render.

1. Go to Render.
2. Create a new Web Service.
3. Connect your GitHub repository.
4. Use these settings:

| Setting | Value |
| --- | --- |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

After Render deploys the project, open:

```text
https://your-render-url.onrender.com/docs
```

That will open Swagger UI for your deployed API.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Swagger UI
- GitHub
- Render

## Final Project Summary

This project is a simple Student Tasks API. It can create, read, update, complete, and delete homework tasks. It is easy to explain because the data is stored in a Python list and all routes are written in one file.
