# Why SQLite? Obviously, you'd use something *much* more robust like PostgreSQL in
# actual production. SQLite handling is built into Python, though, so this avoids the overhead
# of an RDBMS server and driver dependencies for a demo project like this. 
import sqlite3
from . import queries

DBNAME= 'database\\bug_tracker.sqlite'


# Convenience method just so we're not repeating the same database 
# connection/cursor operations everywhere.
# TODO: Error handling. If anything goes wrong, it'll be here.
def execute_query(query_string, query_parameters=None):
	conn = sqlite3.connect(DBNAME)
	cur = conn.cursor()
	if query_parameters is not None:	
		cur.execute(query_string, query_parameters)
	else:
		cur.execute(query_string)
	results = cur.fetchall()
	cur.close()
	conn.commit()
	conn.close()
	return results

# Bug-based methods...

def retrieve_bug_list():
	bug_list = execute_query(queries.BUG_LIST_QUERY)
	return(bug_list)

def retrieve_bug_info(bug_id):
	bug_info = execute_query(queries.SPECIFIC_BUG_QUERY, query_parameters=(bug_id,))
	return(bug_info)

def assign_bug(bug_id, user_id):
	# TODO: Pass something back from this for error handling. 
	execute_query(queries.ASSIGN_BUG_QUERY, query_parameters=(bug_id, user_id))
	return

def close_bug(bug_id):
	# TODO: Pass something back from this when we return for error handling.
	execute_query(queries.CLOSE_BUG_QUERY, query_parameters=(bug_id,))
	return

def create_bug(description, reproduction_steps, severity):
	# TODO: Pass something back from this when we return for error handling.
	execute_query(queries.CREATE_BUG_QUERY, query_parameters=(description, reproduction_steps, severity))
	return	

# User-based methods...
	
def retrieve_user_list():
	user_list = execute_query(queries.USER_LIST_QUERY)
	return user_list
	

def retrieve_user_info(user_id):
	user_info = execute_query(queries.SPECIFIC_USER_QUERY, query_parameters=(user_id,))
	return(user_info)

def create_user(username, first_name, last_name):
	# TODO: Pass something back from this when we return for error handling.
	execute_query(queries.CREATE_USER_QUERY, query_parameters=(username, first_name, last_name))
	return

