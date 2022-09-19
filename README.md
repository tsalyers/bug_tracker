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
As the Flask development server warns you, it's for demo/testing purposes **only**. In production you would use something much more robust to serve your application, like Nginx and Gunicorn. 

### Design decisions
- Why Flask? It's small, it's lightweight, and it's fast to develop in. Something like Django comes with a lot of overhead. 
- Why SQLite? Obviously, you'd use something *much* more robust like PostgreSQL in actual production. SQLite handling is built into Python, though, so this avoids the overhead of an RDBMS server and driver dependencies for a smallish demo project like this. (The application's structured so the underlying database could be pretty easily swapped out, though.)
- Why raw SQL instead of an ORM like SQLAlchemy? I've used ORMs before and generally found that for smaller projects like this they introduce more overhead/dependency than they're worth. I'm not opposed to ORMs, but it's generally faster for me to write in raw SQL, especially if the queries start getting large and complex. 
- Why Jinja2 (the templating engine built into Flask)? This is where I have to confess to being primarily a back-end developer who's been teaching himself front-end skills when he has spare time. In the last year or so I've been trying to learn Vue.js (since it seems to have the least steep learning curve). I'm much more familiar with Flask's templating engine, though, *and* I had a base template I could borrow from an existing project, so that's what I went with. 

### Enhancements for the (hypothetical) future
##### The big things
- Actual production-level infrastructure--i.e., database and webserver. SQLite and the Flask web server are fine for a quick test/demo, but for real-world use you'd want something like PostgreSQL and Nginx/Gunicorn. 
- Some type of access control--logins, permissions, and so on--to restrict the system only to people who should be using it. (I have a current web application that authenticates users against our LDAP server and then checks an internal table for their permissions.)
- Actual logging. This is alluded to in the comments, but in production you'd want your log messages going into a system where they can be catalogued and searched--something like Splunk. 

##### The less-big (but still important) things
- If we're sticking with the template engine, I'd want to re-examine the inheritance hierarchy. Some of them are just similar enough that they could inherit from common ancestors instead of everything inheriting right from the base template. 
- Possibly split up the bug and user functionality into separate Flask blueprints and register them in the main application for neatness. What we have right now isn't bad, but it's starting to border on a little unwieldy. 
- In the user edit screen, we're currently updating the first and last name fields in the database even if they haven't actually changed, which *works*, but isn't ideal. I'd most likely watch for an `onchange` event in the fields and act accordingly.
- Add functionality to assign a bug to a user at bug creation. Currently you have to create a bug, go back to the main bug screen, and then assign it, which is an extra step. 
- Change the "view individual bug/user" requests from GET to POST. Currently the IDs show up in the URL, which isn't terrible--no one should be able to access those URLs without permission--but ideally you don't want IDs like that exposed. 
