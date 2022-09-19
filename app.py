from flask import Flask, request, redirect, render_template
#from . import database_ops as db
from .database import database_ops as db
from .log_ops import write_to_log


# Slight extra step for Pytest.
def create_app():
    app = Flask(__name__)
    return app

# Initialize our app.
# app = Flask(__name__)
app = create_app()


# ----------- Bug-related routes
# Our main page--we default to showing the bug list.
@app.route('/', methods=['GET'])
def list_bugs():
    bugs = db.retrieve_bug_list()
    return render_template('bug_list.html', bug_list=bugs)


# View a specific bug.
@app.route('/view_bug/<bug_id>', methods=['GET'])
def view_bug(bug_id):
    bug_info = db.retrieve_bug_info(bug_id)
    user_list = db.retrieve_user_list()
    return render_template('view_specific_bug.html', bug_info=bug_info, user_list=user_list)


# Close a bug. Doesn't render anything for display--just attempts to close and sends us
# back to the bug list.
@app.route('/close_bug', methods=['POST'])
def close_bug():
    bug_id = request.form.get('bug_id')
    if bug_id:
        db.close_bug(bug_id)
        write_to_log('DEBUG - Closed bug ' + str(bug_id))
    else:
        write_to_log("Error closing bug--ID not found or database error.")

    return redirect('/')


# Assign a bug to a user. Similarly to closing a bug, doesn't display anything.
@app.route('/assign_bug', methods=['POST'])
def assign_bug():
    bug_id = request.form.get('bug_id')
    user_id = request.form.get('user_id')

    if bug_id and user_id:
        db.assign_bug(bug_id, user_id)
    else:
        write_to_log("Error assigning bug--ID not found or database error.")

    return redirect('/')


# Load the "create a new bug" page.
@app.route('/log_new_bug', methods=['GET'])
def log_new_bug():
    return render_template('log_new_bug.html')


# Create the bug (from log_new_bug)in the database and return to the bug list.
@app.route('/create_bug', methods=['POST'])
def create_bug():
    description = request.form.get('description')
    reproduction_steps = request.form.get('reproduction_steps')
    severity = request.form.get('severity')

    if description and reproduction_steps and severity:
        db.create_bug(description, reproduction_steps, severity)
        write_to_log("Attempted to create bug with description '{}'").format(description)
    else:
	    write_to_log("Error creating bug--bug info not found or database error.")
    return redirect('/')


# ----------- User-related routes
@app.route('/list_users', methods=['GET'])
def list_users():
    users = db.retrieve_user_list()
    return render_template('user_list.html', user_list=users)


# View/edit a specific user.
@app.route('/view_user/<user_id>', methods=['GET'])
def view_user(user_id):
    user_info = db.retrieve_user_info(user_id)
    return render_template('view_specific_user.html', user_info=user_info)


# Updates a user's name(s). Doesn't display anything.
@app.route('/update_user', methods=['POST'])
def update_user():
    user_id = request.form.get('user_id')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    if user_id and first_name and last_name:
        db.update_user(first_name, last_name, user_id)
        write_to_log("Updated user {}. Name is now {} {}.".format(user_id, first_name, last_name))
    else:
        write_to_log("Error updating user--ID not found or database error.")

    return redirect('/list_users')


# Load the "create a new user" page.
@app.route('/create_user', methods=['GET'])
def create_user():
    return render_template('create_user.html')


# Add the new user to the database and go back to the user list.
@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('username')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    if username and first_name and last_name:
        db.create_user(username, first_name, last_name)
        write_to_log("Attempted to create user with username {} and name {} {}.".format(username, first_name, last_name))
        write_to_log("If the user has not been created, check that the username does not already exist.")
    else:
        write_to_log("Error updating user--ID not found or database error.")

    return redirect('/list_users')
if __name__ == "__main__":
    app.run()
