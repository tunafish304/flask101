# 1. Project Overview

A simple Flask application with SQLAlchemy for database interaction which demonstrates CRUD (create, read, update, and delete) operations.

This project is built using Flask, a lightweight framework, and SQLAlchemy, an ORM (object relationship modeler) for handling database interactions efficiently.

# 2. Prerequisites

- Python 3.x
- Git installed
- Virtual environment tools (e.g., `venv` or `virtualenv`)

# 3. Steps to Set Up the Virtual Environment using the VS code terminal

Step 1: Clone the repository
git clone https://github.com/tunafish304/flask101.git

Step 2: Navigate to the project directory
cd flask101

Step 3: Create a virtual environment
python -m venv venv

Step 4: Activate the virtual environment
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

# 4. Install Dependencies - use the vs code terminal

pip install flask flask-sqlalchemy

# 5. Run the Application - use the vs code terminal

Instructions for running the Flask app:

# Run the app

python app.py

# Add any additional commands or environment setup, like setting `FLASK_APP` or `FLASK_ENV`:

set FLASK_APP=app.py # Windows
export FLASK_APP=app.py # macOS/Linux
flask run
