# HR System Backend

This is the backend for the HR System, built using Django and Django REST framework. It provides APIs for managing employees and their attendance, with authentication handled by Djoser and token-based authentication.

## Features

- HR employees can log in to the system.
- HR employees can add, edit, and delete other employees.
- HR employees can add attendance records for employees.

### Installation

**Prerequisites**

- Python 3.6+
- Django 3.2+
- Django REST Framework
- Djoser

**Setup**

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Abdulaziz-elitecoder/HR_management_system.git
    cd hr-system-backend
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create and apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

- **admin/**: Admin Page
- **api/**: CRUD Endpoints
- **auth/**: Authentication Endpoints
- **swagger/** [name='schema-swagger-ui']: Swagger Endpoints for better readability
- **redoc/** [name='schema-redoc']: Swagger Documentation Form

