# Bug Tracker
#### A lightweight bug tracking (and user management) system demo

### To install and run

1. Obtain a copy of the source code, either by downloading it in ZIP format and unzipping it into a directory or cloning this repository. 
2. Create a Python virtual environment in the directory containing the source code--e.g. `python -m venv env`. (Python 3.9 was used in development, but any reasonably recent Python should do.)
3. Activate the virtual environment--e.g., `source env/bin/activate` in Linux or `env\scripts\activate` in Windows. 
4. Run `pip install -r requirements.txt` to install dependencies. 
5. Set the environment variable `FLASK_APP` to `app.py`--`export FLASK_APP=app.py` in Linux, `set FLASK_APP=app.py` in Windows. 
6. Run the command `flask run`, and the development server should start. 
7. Visit `http://localhost:5000` to view and work with the application. (Note: 5000 is the default value for the Flask development server port. If you can't connect, check the server's startup message to see if the value is different.)

### A caveat
As the Flask development server warns you, this is for demo/testing purposes **only**. In production you would use something much more robust, like Nginx and Gunicorn. 

### Design decisions
- Why Flask? It's small, it's lightweight, and it's fast to develop in. Something like Django comes with a lot of overhead. 
- Why SQLite? Obviously, you'd use something *much* more robust like PostgreSQL in actual production. SQLite handling is built into Python, though, so this avoids the overhead of an RDBMS server and driver dependencies for a smallish demo project like this. (The application's structured so the underlying database could be pretty easily swapped out, though.)