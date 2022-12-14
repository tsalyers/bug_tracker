# A rough-and-ready API for CRU (there's currently no D) operations on
# bugs and users. Currently just a set of functiions, since this is a small
# single-user application, but they could be REST-ized for a larger system. 


import sqlite3
from . import queries
from ..log_ops import write_to_log

DBNAME = 'database\\bug_tracker.sqlite'


# Convenience method just so we're not repeating the same database
# connection/cursor operations everywhere.
def execute_query(query_string, query_parameters=None):
    results = ()
    try:
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
    except Exception as e:
        # NB: Ideally you'd catch specific exceptions here. We'll cast a wide net for now.
        write_to_log("ERROR--exception occurred in database operation. Error message: {}".format(str(e)))
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


def update_user(user_id, first_name, last_name):
    execute_query(queries.UPDATE_USER_QUERY, query_parameters=(user_id, first_name, last_name))
    return
