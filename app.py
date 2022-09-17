from flask import Flask, flash, request, redirect, url_for, render_template, session
import datetime
from . import database_ops as db


# Initialize our app.
app = Flask(__name__)
#app.secret_key = "I_am_a_long_random_string_of_characters_not_really_change_me"

	
# ----------- Bug-related routes	
# Our main page--we default to showing the bug list.
@app.route('/', methods=['GET'])
def list_bugs():
	bugs = db.retrieve_bug_list()
	return render_template('bug_list.html',bug_list=bugs)

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
		print('DEBUG - Closed bug ' + str(bug_id))
	else:
		flash("Error closing bug--ID not found or database error. Consult your administrator.")
	
	return redirect('/')


# Assign a bug to a user. Similarly to closing a bug, doesn't display anything.	
@app.route('/assign_bug', methods=['POST']) 
def assign_bug():
	bug_id = request.form.get('bug_id')
	user_id = request.form.get('user_id')
	
	if bug_id and user_id:
		db.assign_bug(bug_id, user_id)
		print('DEBUG - assigned bug ' + str(bug_id) + ' to user ' + str(user_id))
	else:
		flash("Error assigning bug--ID not found or database error. Consult your administrator.")	
	
	return redirect('/')


# Create a new bug in the database.
@app.route('/log_new_bug', methods=['GET'])
def log_new_bug():
	return render_template('log_new_bug.html')
	

# Create the bug (from log_new_bug)in the database and return to the bug list.
@app.route('/create_bug', methods=['POST']) 
def create_bug():
	description = request.form.get('description')
	reproduction_steps = request.form.get('reproduction_steps')
	severity = request.form.get('severity')
	
	db.create_bug(description, reproduction_steps, severity)
	return redirect('/') 
	

# ----------- User-related routes	
@app.route('/list_users', methods=['GET'])
def list_users():
	users = db.retrieve_user_list()
	return render_template('user_list.html',user_list=users)	

	
if __name__ == "__main__":
	app.run()