# Put our queries into constants here just because some of these are long and 
# a little messy to put into a method call. 

# Retrieve all open bugs. SQLite doesn't have a boolean type, so we're using 0 for 'closed'
# and 1 for 'open'. 
#
# The left joins are because we'll (most likely) have open bugs, but not every bug will have
# someone assigned yet, so we'll bring back all bug records regardless of their assignment status. 
BUG_LIST_QUERY = '''
		SELECT b.pk1, b.description, b.creation_date, b.severity, u.first_name, u.last_name
		FROM bugs b
                LEFT JOIN bug_assignments ba
		ON b.pk1 = ba.bug_pk1
		LEFT JOIN users u
		ON ba.user_pk1 = u.pk1
		WHERE b.is_open > 0
		'''

# For retrieving individual bugs.
SPECIFIC_BUG_QUERY = '''
		SELECT b.pk1, b.description, b.reproduction_steps, b.creation_date, b.severity, u.first_name, u.last_name
		FROM bugs b
                LEFT JOIN bug_assignments ba
		ON b.pk1 = ba.bug_pk1
		LEFT JOIN users u
		ON ba.user_pk1 = u.pk1
		WHERE b.pk1 = ?
		'''

# For logging new bugs. NB: The creation date defaults to the current timestamp, and we'll be forcing the
# is_open field to 1 ("open"), since we *probably* don't want to immediately close a bug.
CREATE_BUG_QUERY = '''
		INSERT INTO BUGS (description, reproduction_steps, severity, is_open)
		VALUES (?, ?, ?, 1)
		'''

# For closing bugs. Again, SQLite doesn't have a Boolean type, so we use 0 instead. 
CLOSE_BUG_QUERY = '''
		UPDATE BUGS
		SET is_open = 0 
		WHERE pk1 = ?
		'''      

# For assigning bugs to a user. I'm assuming each bug gets assigned to only one user, so I'm using INSERT OR REPLACE 
# to update existing assignments in one step. 
ASSIGN_BUG_QUERY = '''
		INSERT OR REPLACE INTO bug_assignments (bug_pk1, user_pk1)
		VALUES (?, ?)
		'''

# Get our list of users. 
USER_LIST_QUERY = '''
		SELECT pk1, username, first_name, last_name 
		FROM users 
		ORDER BY last_name
		'''

SPECIFIC_USER_QUERY = '''
		SELECT pk1, username, first_name, last_name
		FROM users
		where pk1=?
		'''

CREATE_USER_QUERY = '''
		INSERT INTO users (username, first_name, last_name)
		VALUES (?, ?, ?)
		'''