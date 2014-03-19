import csv

# User creation with name, email, and first 2 picks.
def add_user():
	# Get user's name and email for the first time
	user_name = raw_input("Please enter your name: ")
	user_email = raw_input("Enter your email so we can send you results and instructions: ")
	user_account = [user_name, user_email]

	# Check if information is correct.
	print "Is this the correct name and email?", user_name, user_email
	answer = raw_input("Print 'Y' or 'N':")
	if answer == 'Y' or answer == 'y':
		# Add user to user csv
		with open('knockout.csv', 'ab') as db:
			print "Starting to append data"
			a = csv.writer(db, delimiter=',')
			a.writerow(user_account)

		db.close()
		print "Done writing data"
	else:
		print "No problem, let's start from the beginning."
		add_user()

# Calling function to add a user
add_user()