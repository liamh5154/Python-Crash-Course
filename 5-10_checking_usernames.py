#	If Statements - 5-10 Checking Usernames pg93
"""Do the following to create a program that simulates how websites ensure
that everyone has a unique username."""

current_users = ['admin', 'mike', 'ross', 'alex', 'matt']
new_users = ['joe', 'craig', 'jack', 'ALEX', 'Matt']

for new_user in new_users:
	if new_user.lower() in current_users:
		print("Sorry, " + new_user.title() + " is already taken. Please choose another username.")
	else:
		print(new_user.title() + " is available.")
