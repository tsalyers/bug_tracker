from datetime import datetime

# Convenience method for logging. 
def get_timestamp():
	return str(datetime.now()) + " "
	
# NB: In production, you would have a dedicated logging service--ELK, Splunk, etc.
# Here, we'll just print to standard output. 
def write_to_log(message):
	print(get_timestamp() + message)