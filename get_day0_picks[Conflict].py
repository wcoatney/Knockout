import csv

def get_day0_picks():
	# Get email address so that the picks are added to the right user
	cross_check_email = raw_input("Enter the email address you used to make your Knockout account: ")

	# Make a new list that will hold the users email addresses so we can crosscheck
	csv_holder = csv.reader(open('knockout.csv', 'rU'))
	email_holder = []
	file_loop = [l for l in csv_holder]

	# Add the email address to the email_holder
	for item in file_loop:
		email_holder.append(item[1])

	# # Check all the emails for the address the user gave us to crosscheck
	# for address in email_holder:
		
	# If there is a match add the list of picks, 'new_picks', to users list_of_picks
	if cross_check_email in email_holder:
		dex_checker = email_holder.index(cross_check_email)
		# Make sure dex_checker is correct
		# print dex_checker		
		
		# Get the two picks from the user
		pick1 = raw_input("Enter your first pick for the March 20th games: ")
		pick2 = raw_input("Enter your second pick for the March 20th games: ")

		# Make a list of users new picks
		new_picks = []
		new_picks.append(pick1)
		new_picks.append(pick2)

		# Add the picks to the user's list_of_picks
		print "We found your account and are adding your picks"
		file_loop[dex_checker][3] = new_picks
		with open('knockout.csv', 'w') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerows(file_loop)
			fp.close()
			print "Your picks for the March 20th games have been added. Good luck!"
		
	# If there is not a match, then prompt the user to enter another email
	else:
		print "We did not find the email you gave us, try entering another email address."

# Calling function to add user's picks on Thursday, March 20th, 2014
get_day0_picks()