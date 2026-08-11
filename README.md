# Task Flow

Task Flow is a Django web application for managing workers and tasks in a software development team.

The application provides a simple interface for managing workers, positions, task types, and tasks. Tasks can be assigned to multiple workers, have different priorities and deadlines, and can be marked as completed.

The project is built with Django and uses SQLite as the database.

## Features

* Worker management
* Position management
* Task type management
* Task management
* Assign tasks to multiple workers
* Task priorities
* Task deadlines
* Task completion status
* Task descriptions
* Worker detail pages with assigned tasks
* Django administration panel
* Unit and integration tests
* Docker support

## Technologies

* Python 3.11
* Django 5.2.17
* SQLite
* Docker
* Docker Compose
* Django Templates
* Django Test Framework

## Models

The project contains the following main models:

### Position

Represents a worker's position in the company.

Examples:

* Developer
* Manager
* Designer

### Worker

Represents an employee who can be assigned to tasks.

A worker contains:

* username
* first name
* last name
* email
* password
* position

Workers use Django's authentication system.

### TaskType

Represents the type or category of a task.

Examples:

* Bug
* Feature
* Improvement

### Task

Represents a task that needs to be completed.

A task contains:

* name
* description
* deadline
* priority
* completion status
* task type
* assigned workers

## Project Structure

```text
py-task-flow/
│
├── task_flow/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/danyatatarchuk/py-task-flow.git
```

Navigate to the project directory:

```bash
cd py-task-flow
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment.

On macOS/Linux:

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

## Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/tasks/
```

## Admin Panel

The project includes the Django administration panel.

Create a superuser:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/admin/
```

## Docker

The project supports running the application with Docker and Docker Compose.

Make sure Docker Desktop is installed and running.

Build and start the application:

```bash
docker compose up --build
```

The application will be available at:

```text
http://127.0.0.1:8000/tasks/
```

To stop the application:

```bash
docker compose down
```

The project uses SQLite, so no additional database container is required.

## Tests

The project contains tests for models and views.

Run all tests:

```bash
python manage.py test
```

The current test suite contains 11 tests covering:

* Position model
* Worker model
* TaskType model
* Task model
* Worker list view
* Worker detail view
* Task list view
* Task detail view
* Task creation
* Task update
* Task deletion

Expected result:

```text
Found 11 test(s).
...........
----------------------------------------------------------------------
Ran 11 tests ... 

OK
```

## Main URLs

### Workers

```text
/tasks/workers/
```

List of all workers.

### Worker Details

```text
/tasks/workers/<worker_id>/
```

Details about a specific worker and their assigned tasks.

### Tasks

```text
/tasks/tasks/
```

List of all tasks.

### Task Details

```text
/tasks/tasks/<task_id>/
```

Details about a specific task.

### Create Task

```text
/tasks/tasks/create/
```

Create a new task.

### Update Task

```text
/tasks/tasks/<task_id>/update/
```

Update an existing task.

### Delete Task

```text
/tasks/tasks/<task_id>/delete/
```

Delete an existing task.

### Django Admin

```text
/admin/
```

## Development

The project uses Django's built-in development server during local development.

For local development:

```bash
python manage.py runserver
```

For Docker:

```bash
docker compose up --build
```

## License

This project was created for educational and portfolio purposes.
