import csv

# Set each user's status based on if their current picks are in 'list_of_winners.csv'
def set_dead_or_alive:
	# Make a new list that will hold the users email addresses so we can crosscheck
	csv_holder = csv.reader(open('knockout.csv', 'rU'))
	email_holder = []
	file_loop = [l for l in csv_holder]

	# Add the email address to the email_holder
	for item in file_loop:
		email_holder.append(item[3])