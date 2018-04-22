#	If Statements - 5-8/5-9 Hello Admin pg93
"""Make a list of 5 or more usernames including the name 'admin'.
Imagine you are writing code that will print a greeting to each user after
they log into a website. Loop through the list and print a greeting to 
each user."""
usernames = ['admin', 'ross', 'mike', 'alex', 'matt']
if usernames:
	for username in usernames:
		if username == 'admin':
			print("Hello Admin, would you like to see a status report?")
		else:
			print("Hello " + username.title() + ", welcome back.")
else:
	("There are no registered users.")
print('\n')

usernames_0 = []
if usernames_0:
	for username in usernames_0:
		if username == 'admin':
			print("Hello Admin, would you like to see a status report?")
		else:
			print("Hello " + username.title() + ", welcome back.")
else:
	print("There are no registered users.")
