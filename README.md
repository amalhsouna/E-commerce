# Flask Application Setup and Instructions

This guide explains how to set up a Flask application, manage dependencies, handle migrations, and write tests.

---

## Setting Up the Environment

1. **Create a virtual environment**:  
   ```bash
   python -m venv <environment_name>

2. **Activate the virtual environment**:  
    ```bash
   .\<environment_name>\Scripts\activate

2. **Install Flask**:  
   ```bash
   pip install flask

   Save dependencies to requirements.txt:
   ```bash
   pip install -r requirements.txt
   pip freeze > requirements.txt

3. **Install envirenement variables**:  
   ```bash
   pip install python-dotenv

  After installation, update the requirements.txt:
    ```bash

    pip freeze > requirements.txt

4. **Install SQLAlchemy && PostgreSQL**:  
    Database and ORM Setup
    Install SQLAlchemy:

    ```bash
    pip install flask-SQLAlchemy
    
    Install PostgreSQL Adapter:
    Use psycopg2-binary to interact with PostgreSQL:

    ```bash
    pip install psycopg2-binary

    Install migration tools:

5. **Install Migrate**:
    ```bash
    pip install alembic Flask-Migrate
    Initialize migrations:

    ```bash
    flask db init
    Create a migration:

    ```bash
    flask db migrate -m "initial migration"
    Apply the migration:

    ```bash
    flask db upgrade

6. ** Writing Tests**:
    Install Testing Tools
    To write unit and functional tests, install pytest and Flask-Testing:

    ```bash
    pip install pytest flask-testing
    Run Tests

    To execute all tests:

    ```bash
    pytest









