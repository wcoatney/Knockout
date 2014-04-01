import csv

# User creation with name, email, and first 2 picks.
def add_user():
	# Get user's name and email for the first time
	user_name = raw_input("Please enter your name: ")
	user_email = raw_input("Enter your email so we can send you results and instructions: ")
	user_account = [user_name, user_email]
	blank_filler = ["empty","empty","empty","empty","empty","empty","empty","empty"]
	add_user = []

	# Make a new list that will hold the users email addresses so we can crosscheck
	csv_holder = csv.reader(open('knockout.csv', 'rU'))

	# Place each row and column into raw_people
	raw_people = [l for l in csv_holder]

	# Check if information is correct.
	print "Is this the correct name and email?", user_name, user_email
	answer = raw_input("Print 'Y' or 'N':")
	if answer == 'Y' or answer == 'y':
		# Adding user_account items and blank_filter items to add_user
		add_user.extend(user_account)
		add_user.extend(blank_filler)
		print add_user # debugging
		with open('knockout.csv', 'ab') as db:
			print "Starting to append data"
			a = csv.writer(db, delimiter=',')
			a.writerow(add_user)
		db.close()
		
		print "Done writing user data and filler content"
	else:
		print "No problem, let's start from the beginning."
		add_user()

# Calling function to add a user
# add_user()

# Check to make sure pick1 have not been picked in the past and are still in the tourney
def check_pick1(pick1):	
	# Make a new list that will hold the list_of_winners so we can crosscheck
	csv_holder = csv.reader(open('list_of_winners.csv', 'rU'))
	
	# Place each row and column into file_loop	
	file_loop = [l for l in csv_holder]

	# Make a new list that will hold the list_of_winners so we can crosscheck
	winners_holder = []
	
	# Make list for old_picks
	old_picks_holder = []
	
	# Put the old_picks of the correct user (dex_checker) into old_picks_holder
	old_picks_holder = [file_loop[dex_checker][9]]

	# Add the winners to the winners_holder
	for item in file_loop:
		winners_holder.append(item[0])

	# Check to see if pick1 is in list of old_picks and not in winners_holder
	if pick1 in old_picks_holder:
		print 'You have already picked', pick1, '. You can only pick a team once.'
		pick1 = raw_input("Enter your first pick for the March 20th games: ")
	# Check to make sure that this pick is playing today
	elif pick1 not in winners_holder:
		print pick1, " is not in the tourney anymore. Let's start over."
		pick1 = raw_input("Enter your first pick for the March 20th games: ")

# Function to add user's picks on Thursday, March 20th, 2014
def get_day0_picks():
	# Get email address so that the picks are added to the right user
	cross_check_email = raw_input("Enter the email address you used to make your Knockout account: ")

	# Make a new list that will hold the users email addresses so we can crosscheck
	csv_holder = csv.reader(open('knockout.csv', 'rU'))
	# Place each row and column into file_loop
	raw_people = [l for l in csv_holder]
	# Make a new list that will hold the users email addresses so we can crosscheck
	email_holder = []
	# Add the email address to the email_holder
	for item in raw_people:
		email_holder.append(item[1])


	# Make list of winners to check picks against
	csv_holder = csv.reader(open('list_of_winners.csv', 'rU'))
	raw_winners = [l for l in csv_holder]
	winners_holder = []
	for item in raw_winners:
		winners_holder.append(item[0])

	# # Check all the emails for the address the user gave us to crosscheck
	# for address in email_holder:
		
	# If there is a match add the list of picks, 'new_picks', to users list_of_picks
	if cross_check_email in email_holder:
		dex_checker = email_holder.index(cross_check_email)
		# Make sure dex_checker is correct
		print "%s index is %s: " % (raw_people[dex_checker][0],dex_checker)		
		
		# Get the first pick from the user
		pick1 = raw_input("Enter your first pick for the March 20th games: ")

		# Check to make sure pick1 is legal
		# check_pick1(pick1)
		
		# Keep asking for pick1 until it is in winners_holder
		while pick1 not in winners_holder:
			pick1 = raw_input("Make sure you pick a team that's in the tourney: ")
		
		# Get the second pick from the user
		pick2 = raw_input("Enter your second pick for the March 20th games: ")

		# Keep asking for pick1 until it is in winners_holder
		while pick2 not in winners_holder:
			pick2 = raw_input("Make sure you pick a team that's in the tourney: ")

		print "Pick number 1 for %s is: %s" % (raw_people[dex_checker][0],pick1)
		print "Pick number 2 for %s is: %s" % (raw_people[dex_checker][0],pick2)

		# Check to make sure pick2 is legal
		# check_pick2(pick2)

		# Add the picks to the raw_people
		print "We found your account and are adding your picks"
		raw_people[dex_checker][3] = pick1
		raw_people[dex_checker][4] = pick2

		# Write the raw_people with pick1 and pick2 to knockout.csv
		with open('knockout.csv', 'wb') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerow(raw_people)
			fp.close()
			print "Your picks for the March 20th games have been added. Good luck!"
		
	# If there is not a match, then prompt the user to enter another email
	else:
		print "We did not find the email you gave us, try entering another email address."
		get_day0_picks()

# Calling function to add user's first 2 picks on Thursday, March 20th, 2014
get_day0_picks()

def check_pick2(pick2):
	# Make list for old_picks
	old_picks_holder = []
	
	# Put the old_picks of the correct user (dex_checker) into old_picks_holder
	old_picks_holder = [file_loop[dex_checker][9]]
	
	# Make a new list that will hold the list_of_winners so we can crosscheck
	csv_holder = csv.reader(open('list_of_winners.csv', 'rU'))
	
	# Make a new list that will hold the list_of_winners so we can crosscheck
	winners_holder = []
	
	# Place each row and column into file_loop
	file_loop = [l for l in csv_holder]

	# Add the winners to the winners_holder
	for item in file_loop:
		winners_holder.append(item[0])

	# Check to see if pick2 is in list of old_picks and not in winners_holder
	if pick2 in old_picks_holder:
		print 'You have already picked', pick2, '. You can only pick a team once.'
		pick2 = raw_input("Enter your second pick for the March 20th games: ")
	# Check to make sure that this pick is playing today
	elif pick2 not in winners_holder:
		print pick2, " is not in the tourney anymore. Let's start over."
		pick2 = raw_input("Enter your second pick for the March 20th games: ")

def check_pick3(pick3):
	# Make list for old_picks
	old_picks_holder = []
	
	# Put the old_picks of the correct user (dex_checker) into old_picks_holder
	old_picks_holder = [file_loop[dex_checker][9]]
	
	# Make a new list that will hold the list_of_winners so we can crosscheck
	csv_holder = csv.reader(open('list_of_winners.csv', 'rU'))
	
	# Make a new list that will hold the list_of_winners so we can crosscheck
	winners_holder = []
	
	# Place each row and column into file_loop	
	file_loop = [l for l in csv_holder]

	# Add the winners to the winners_holder
	for item in file_loop:
		winners_holder.append(item[0])

	# Check to see if pick3 is in list of old_picks and not in winners_holder
	if pick3 in old_picks_holder:
		print 'You have already picked', pick3, '. You can only pick a team once.'
		pick3 = raw_input("Enter your third pick: ")
	# Check to make sure that this pick is playing today
	elif pick3 not in winners_holder:
		print pick3, " is not in the tourney anymore. Let's start over."
		pick3 = raw_input("Enter your third pick: ")

def check_pick4(pick4):
	# Make list for old_picks
	old_picks_holder = []
	
	# Put the old_picks of the correct user (dex_checker) into old_picks_holder
	old_picks_holder = [file_loop[dex_checker][9]]
	
	# Make a new list that will hold the list_of_winners so we can crosscheck
	csv_holder = csv.reader(open('list_of_winners.csv', 'rU'))
	
	# Make a new list that will hold the list_of_winners so we can crosscheck
	winners_holder = []
	
	# Place each row and column into file_loop	
	file_loop = [l for l in csv_holder]

	# Add the winners to the winners_holder
	for item in file_loop:
		winners_holder.append(item[0])

	# Check to see if pick4 is in list of old_picks and not in winners_holder
	if pick4 in old_picks_holder:
		print 'You have already picked', pick4, '. You can only pick a team once.'
		pick4 = raw_input("Enter your fourth pick: ")
	# Check to make sure that this pick is playing today		
	elif pick4 not in winners_holder:
		print pick4, " is not in the tourney anymore. Let's start over."
		pick4 = raw_input("Enter your fourth pick: ")

def check_pick5(pick5):
	# Make list for old_picks
	old_picks_holder = []
	
	# Put the old_picks of the correct user (dex_checker) into old_picks_holder
	old_picks_holder = [file_loop[dex_checker][9]]
	
	# Make a new list that will hold the list_of_winners so we can crosscheck
	csv_holder = csv.reader(open('list_of_winners.csv', 'rU'))
	
	# Make a new list that will hold the list_of_winners so we can crosscheck
	winners_holder = []
	
	# Place each row and column into file_loop	
	file_loop = [l for l in csv_holder]

	# Add the winners to the winners_holder
	for item in file_loop:
		winners_holder.append(item[0])

	# Check to see if pick5 is in list of old_picks and not in winners_holder
	if pick5 in old_picks_holder:
		print 'You have already picked', pick5, '. You can only pick a team once.'
		pick5 = raw_input("Enter your fifth pick: ")
	# Check to make sure that this pick is playing today
	elif pick5 not in winners_holder:
		print pick5, " is not in the tourney anymore. Let's start over."
		pick5 = raw_input("Enter your fifth pick: ")

def check_pick6(pick6):
	# Make list for old_picks
	old_picks_holder = []
	
	# Put the old_picks of the correct user (dex_checker) into old_picks_holder
	old_picks_holder = [file_loop[dex_checker][9]]
	
	# Make a new list that will hold the list_of_winners so we can crosscheck
	csv_holder = csv.reader(open('list_of_winners.csv', 'rU'))
	
	# Make a new list that will hold the list_of_winners so we can crosscheck
	winners_holder = []
	
	# Place each row and column into file_loop	
	file_loop = [l for l in csv_holder]

	# Add the winners to the winners_holder
	for item in file_loop:
		winners_holder.append(item[0])

	# Check to see if pick6 is in list of old_picks and not in winners_holder
	if pick6 in old_picks_holder:
		print 'You have already picked', pick6, '. You can only pick a team once.'
		pick6 = raw_input("Enter your sixth pick: ")
	# Check to make sure that this pick is playing today
	elif pick6 not in winners_holder:
		print pick6, " is not in the tourney anymore. Let's start over."
		pick6 = raw_input("Enter your sixth pick: ")

# Set each user's status to either 'dead' or 'alive' 
# based on whether or not their current picks are in 'list_of_winners.csv'
def set_status_day0():
	file1 = csv.reader(open('knockout.csv', "rU")) # Opening 'knockout.csv' and setting to file1
	file2 = csv.reader(open('list_of_winners.csv', "rU")) # Opening 'list_of_winners.csv' and setting to file2

	raw_people = [l for l in file1]
	raw_winners = [l for l in file2]
	clean_winners = []


	print "Here are the users first picks:" # Debugging
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
	for item in raw_people:
		dex = raw_people.index(item)
		print "%s's first pick is: %s" % (raw_people[dex][0], raw_people[dex][3])

	print "Here are the users second picks:" # Debugging
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	for item in raw_people:
		dex = raw_people.index(item)
		print "%s's second pick is: %s" % (raw_people[dex][0], raw_people[dex][4])

	print raw_winners # debugging

	print "Here are the list of winners:" # Debugging
	for item in raw_winners:
		dex = raw_winners.index(item)
		print "%s" % raw_winners[dex][0]
		clean_winners.append(raw_winners[dex][0])

	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	print "Here's who passed the second round:"
	for item in raw_people:
		dex = raw_people.index(item)
		status = raw_people[dex][2]
		print "%s's status before checking is: %s" % (raw_people[dex][0], status) # debugging

		if item[3] in clean_winners: # index of the first pick
			if item[4] in clean_winners: # index of the second pick
				print "%r passed - we checked" % item[0] # debugging
				# Write 'alive' to this user's status - status is column[2]
				raw_people[dex][2] = 'alive'
			else:
				print "%r lost - we checked" % item[0] #debugging
				# Write 'dead' to this user's status - status is column[2]
				raw_people[dex][2] = 'dead'
		else:
			print "%r lost - we checked" % item[0] #debugging
			# Write 'dead' to this user's status - status is column[2]
			raw_people[dex][2] = 'dead'
	print "Finished checking picks and setting statuses."

	print "Attempting to write the status of each user to the database"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	# Writing correct status to 'knockout.csv'
	with open('knockout.csv', 'wb') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(raw_people)
		fp.close()
		print "Successfully wrote dead or alive to each user."

# set_status_day0()

# Function to add user's picks on Friday, March 21th, 2014
def get_day1_picks():
	# Get email address so that the picks are added to the right user
	cross_check_email = raw_input("Enter the email address you used to make your Knockout account: ")
	
	# Make a new list that will hold the users email addresses so we can crosscheck
	email_holder = []

	# Make a new list that will hold the users email addresses so we can crosscheck
	file1 = csv.reader(open('knockout.csv', 'rU'))
		
	# Place each row and column into raw_people
	raw_people = [l for l in file1]

	# Add the email address to the email_holder
	for item in raw_people:
		email_holder.append(item[1])

	# # Check all the emails for the address the user gave us to crosscheck
	# for address in email_holder:
		
	# If there is a match add the list of picks, 'new_picks', to users list_of_picks
	if cross_check_email in email_holder:
		dex = email_holder.index(cross_check_email)
		# Make sure dex is correct
		# print dex

		status = raw_people[dex][2]

		if status == 'alive':
			# Get the first pick from the user
			pick1 = raw_input("Enter your first pick: ")			
			# Check to make sure pick1 is legal
			check_pick1(pick1)
			# Get the second pick from the user
			pick2 = raw_input("Enter your second pick: ")
			# Check to make sure pick2 is legal
			check_pick2(pick2)
			
			# Add the picks to the raw_people
			print "We found your account and are adding your picks"
			raw_people[dex][3] = pick1
			raw_people[dex][4] = pick2
		else:
			print "Since you lost the last round you must make 4 picks this round."
			# Get the first pick from the user
			pick1 = raw_input("Enter your first pick: ")			
			# Check to make sure pick1 is legal
			check_pick1(pick1)
			# Get the second pick from the user
			pick2 = raw_input("Enter your second pick: ")
			# Check to make sure pick2 is legal
			check_pick2(pick2)
			# Get the third pick from the user
			pick3 = raw_input("Enter your third pick: ")
			# Check to make sure pick3 is legal
			check_pick3(pick3)
			# Get the fourth pick from the user
			pick4 = raw_input("Enter your fourth pick: ")
			# Check to make sure pick4 is legal
			check_pick4(pick4)
			
			# Add the picks to the raw_people
			print "We found your account and are adding your picks"
			raw_people[dex][3] = pick1
			raw_people[dex][4] = pick2
			raw_people[dex][5] = pick3
			raw_people[dex][6] = pick4

		# Write the raw_people to knockout.csv
		with open('knockout.csv', 'ab') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerow(raw_people)
			fp.close()
			print "Your picks for the March 21st games have been added. Good luck!"
		
	# If there is not a match, then prompt the user to enter another email
	else:
		print "We did not find the email you gave us, try entering another email address."

# Calling function to add user's picks for Friday, March 21th, 2014
# get_day1_picks()	

# Set each user's status to either 'dead' or 'alive' 
# based on whether or not their current picks are in 'list_of_winners.csv'
def set_status_day1():
	file1 = csv.reader(open('knockout.csv', "rU")) # Opening 'knockout.csv' and setting to file1
	file2 = csv.reader(open('list_of_winners.csv', "rU")) # Opening 'list_of_winners.csv' and setting to file2

	raw_people = [l for l in file1]
	raw_winners = [l for l in file2]
	clean_winners = []


	print "Here are the users first picks:" # Debugging
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
	for item in raw_people:
		dex = raw_people.index(item)
		print "%s's first pick is: %s" % (raw_people[dex][0], raw_people[dex][3])

	print "Here are the users second picks:" # Debugging
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	for item in raw_people:
		dex = raw_people.index(item)
		print "%s's second pick is: %s" % (raw_people[dex][0], raw_people[dex][4])

	print raw_winners # debugging

	print "Here are the list of winners:" # Debugging
	for item in raw_winners:
		dex = raw_winners.index(item)
		print "%s" % raw_winners[dex][0]
		clean_winners.append(raw_winners[dex][0])

	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	print "Here's who passed the second round:"
	for item in raw_people:
		dex = raw_people.index(item)
		status = raw_people[dex][2]
		print "%s's status before checking is: %s" % (raw_people[dex][0], status) # debugging

		if status == 'alive': # Check to see user's status, if 'alive', only check two picks - column[3] thru column[4]
			if item[3] in clean_winners: # index of the first pick
				if item[4] in clean_winners: # index of the second pick
					print "%r passed - we checked" % item[0] # debugging
					# Write 'alive' to this user's status - status is column[2]
					raw_people[dex][2] = 'alive'
				else:
					print "%r lost - we checked" % item[0] #debugging
					# Write 'dead' to this user's status - status is column[2]
					raw_people[dex][2] = 'dead'
			else:
				print "%r lost - we checked" % item[0] #debugging
				# Write 'dead' to this user's status - status is column[2]
				raw_people[dex][2] = 'dead'
		else: # If the user's status is 'dead' then check four picks column[3] thru column[6]
			if item[3] in clean_winners:
				if item[4] in clean_winners:
					if item[5] in clean_winners:
						if item[6] in clean_winners:
							print "%r passed - we checked" % item[0] # debugging
							# Write 'alive' to this user's status - status in column[2]
							raw_people[dex][2] = 'alive'
			else:
				print "%r lost - we checked" % item[0] # debugging
				# Write 'dead' to this user's status - status is column[2]
				raw_people[dex][2] = 'dead'
	print "Finished checking picks and setting statuses."

	print "Attempting to write the status of each user to the database"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	# Writing correct status to 'knockout.csv'
	with open('knockout.csv', 'wb') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(raw_people)
		fp.close()
		print "Successfully wrote dead or alive to each user."

# set_status_day1()

# Function to add user's picks on Saturday, March 22th, 2014
def get_day2_picks():
	# Get email address so that the picks are added to the right user
	cross_check_email = raw_input("Enter the email address you used to make your Knockout account: ")
	
	# Make a new list that will hold the users email addresses so we can crosscheck
	email_holder = []

	# Make a new list that will hold the users email addresses so we can crosscheck
	file1 = csv.reader(open('knockout.csv', 'rU'))
		
	# Place each row and column into raw_people
	raw_people = [l for l in file1]

	# Add the email address to the email_holder
	for item in raw_people:
		email_holder.append(item[1])

	# # Check all the emails for the address the user gave us to crosscheck
	# for address in email_holder:
		
	# If there is a match add the list of picks, 'new_picks', to users list_of_picks
	if cross_check_email in email_holder:
		dex = email_holder.index(cross_check_email)
		# Make sure dex is correct
		# print dex

		status = raw_people[dex][2]

		if status == 'alive':
			# Get the first pick from the user
			pick1 = raw_input("Enter your first pick: ")			
			# Check to make sure pick1 is legal
			check_pick1(pick1)
			
			# Add the pick to raw_people
			print "We found your account and are adding your picks"
			raw_people[dex][3] = pick1
		else:
			print "Since you lost the last round you must make 4 picks this round."
			# Get the first pick from the user
			pick1 = raw_input("Enter your first pick: ")			
			# Check to make sure pick1 is legal
			check_pick1(pick1)
			# Get the second pick from the user
			pick2 = raw_input("Enter your second pick: ")
			# Check to make sure pick2 is legal
			check_pick2(pick2)
			# Get the third pick from the user
			pick3 = raw_input("Enter your third pick: ")
			# Check to make sure pick3 is legal
			check_pick3(pick3)
			# Get the fourth pick from the user
			pick4 = raw_input("Enter your fourth pick: ")
			# Check to make sure pick4 is legal
			check_pick4(pick4)
			# Get the fifth pick from the user
			pick5 = raw_input("Enter your fifth pick: ")
			# Check to make sure pick5 is legal
			check_pick5(pick5)
			
			# Add the picks to the raw_people
			print "We found your account and are adding your picks"
			raw_people[dex][3] = pick1
			raw_people[dex][4] = pick2
			raw_people[dex][5] = pick3
			raw_people[dex][6] = pick4
			raw_people[dex][7] = pick5

		# Write the raw_people to knockout.csv
		with open('knockout.csv', 'ab') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerow(raw_people)
			fp.close()
			print "Your picks for the March 22th games have been added. Good luck!"
		
	# If there is not a match, then prompt the user to enter another email
	else:
		print "We did not find the email you gave us, try entering another email address."

# Calling function to add user's picks for Saturday, March 22th, 2014
# get_day2_picks()

def set_status_day2():
	file1 = csv.reader(open('knockout.csv', "rU")) # Opening 'knockout.csv' and setting to file1
	file2 = csv.reader(open('list_of_winners.csv', "rU")) # Opening 'list_of_winners.csv' and setting to file2

	raw_people = [l for l in file1]
	raw_winners = [l for l in file2]
	clean_winners = []


	print "Here are the users first picks:" # Debugging
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
	for item in raw_people:
		dex = raw_people.index(item)
		print "%s's first pick is: %s" % (raw_people[dex][0], raw_people[dex][3])

	print "Here are the users second picks:" # Debugging
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	for item in raw_people:
		dex = raw_people.index(item)
		print "%s's second pick is: %s" % (raw_people[dex][0], raw_people[dex][4])

	print raw_winners # debugging

	print "Here are the list of winners:" # Debugging
	for item in raw_winners:
		dex = raw_winners.index(item)
		print "%s" % raw_winners[dex][0]
		clean_winners.append(raw_winners[dex][0])

	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	print "Here's who passed the third round:"
	for item in raw_people:
		dex = raw_people.index(item)
		status = raw_people[dex][2]
		print "%s's status before checking is: %s" % (raw_people[dex][0], status) # debugging

		if status == 'alive': # Check to see user's status, if 'alive', only check one pick - column[3]
			if item[3] in clean_winners: # index of the first pick
				print "%r passed - we checked" % item[0] # debugging
				# Write 'alive' to this user's status - status is column[2]
				raw_people[dex][2] = 'alive'
			else:
				print "%r lost - we checked" % item[0] #debugging
				# Write 'dead' to this user's status - status is column[2]
				raw_people[dex][2] = 'dead'
		else: # If the user's status is 'dead' then check five picks column[3] thru column[7]
			if item[3] in clean_winners:
				if item[4] in clean_winners:
					if item[5] in clean_winners:
						if item[6] in clean_winners:
							if item[7] in clean_winners:
								print "%r passed - we checked" % item[0] # debugging
								# Write 'alive' to this user's status - status in column[2]
								raw_people[dex][2] = 'alive'
			else:
				print "%r lost - we checked" % item[0] # debugging
				# Write 'dead' to this user's status - status is column[2]
				raw_people[dex][2] = 'dead'
	print "Finished checking picks and setting statuses."

	print "Attempting to write the status of each user to the database"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	# Writing correct status to 'knockout.csv'
	with open('knockout.csv', 'wb') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(raw_people)
		fp.close()
		print "Successfully wrote dead or alive to each user."

# set_status_day2()

# Function to add user's picks on Sunday, March 23th, 2014
def get_day3_picks():
	# Get email address so that the picks are added to the right user
	cross_check_email = raw_input("Enter the email address you used to make your Knockout account: ")
	
	# Make a new list that will hold the users email addresses so we can crosscheck
	email_holder = []

	# Make a new list that will hold the users email addresses so we can crosscheck
	file1 = csv.reader(open('knockout.csv', 'rU'))
		
	# Place each row and column into raw_people
	raw_people = [l for l in file1]

	# Add the email address to the email_holder
	for item in raw_people:
		email_holder.append(item[1])

	# # Check all the emails for the address the user gave us to crosscheck
	# for address in email_holder:
		
	# If there is a match add the list of picks, 'new_picks', to users list_of_picks
	if cross_check_email in email_holder:
		dex = email_holder.index(cross_check_email)
		# Make sure dex is correct
		# print dex

		status = raw_people[dex][2]

		if status == 'alive':
			# Get the first pick from the user
			pick1 = raw_input("Enter your first pick: ")			
			# Check to make sure pick1 is legal
			check_pick1(pick1)
			
			# Add the pick to raw_people
			print "We found your account and are adding your picks"
			raw_people[dex][3] = pick1
		else:
			print "Since you lost the last round you must make 6 picks this round."
			# Get the first pick from the user
			pick1 = raw_input("Enter your first pick: ")			
			# Check to make sure pick1 is legal
			check_pick1(pick1)
			# Get the second pick from the user
			pick2 = raw_input("Enter your second pick: ")
			# Check to make sure pick2 is legal
			check_pick2(pick2)
			# Get the third pick from the user
			pick3 = raw_input("Enter your third pick: ")
			# Check to make sure pick3 is legal
			check_pick3(pick3)
			# Get the fourth pick from the user
			pick4 = raw_input("Enter your fourth pick: ")
			# Check to make sure pick4 is legal
			check_pick4(pick4)
			# Get the fifth pick from the user
			pick5 = raw_input("Enter your fifth pick: ")
			# Check to make sure pick5 is legal
			check_pick5(pick5)
			# Get the sixth pick from the user
			pick6 = raw_input("Enter your sixth pick: ")
			# Check to make sure pick6 is legal
			check_pick6(pick6)
			
			# Add the picks to the raw_people
			print "We found your account and are adding your picks"
			raw_people[dex][3] = pick1
			raw_people[dex][4] = pick2
			raw_people[dex][5] = pick3
			raw_people[dex][6] = pick4
			raw_people[dex][7] = pick5
			raw_people[dex][8] = pick6

		# Write the raw_people to knockout.csv
		with open('knockout.csv', 'ab') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerow(raw_people)
			fp.close()
			print "Your picks for the March 23rd games have been added. Good luck!"
		
	# If there is not a match, then prompt the user to enter another email
	else:
		print "We did not find the email you gave us, try entering another email address."

# Calling function to add user's picks for Sunday, March 23th, 2014
# get_day3_picks()

def set_status_day3():
	file1 = csv.reader(open('knockout.csv', "rU")) # Opening 'knockout.csv' and setting to file1
	file2 = csv.reader(open('list_of_winners.csv', "rU")) # Opening 'list_of_winners.csv' and setting to file2

	raw_people = [l for l in file1]
	raw_winners = [l for l in file2]
	clean_winners = []


	print "Here are the users first picks:" # Debugging
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
	for item in raw_people:
		dex = raw_people.index(item)
		print "%s's first pick is: %s" % (raw_people[dex][0], raw_people[dex][3])

	print "Here are the users second picks:" # Debugging
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	for item in raw_people:
		dex = raw_people.index(item)
		print "%s's second pick is: %s" % (raw_people[dex][0], raw_people[dex][4])

	print raw_winners # debugging

	print "Here are the list of winners:" # Debugging
	for item in raw_winners:
		dex = raw_winners.index(item)
		print "%s" % raw_winners[dex][0]
		clean_winners.append(raw_winners[dex][0])

	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	print "Here's who passed the fourth round:"
	for item in raw_people:
		dex = raw_people.index(item)
		status = raw_people[dex][2]
		print "%s's status before checking is: %s" % (raw_people[dex][0], status) # debugging

		if status == 'alive': # Check to see user's status, if 'alive', only check one pick - column[3]
			if item[3] in clean_winners: # index of the first pick
				print "%r passed - we checked" % item[0] # debugging
				# Write 'alive' to this user's status - status is column[2]
				raw_people[dex][2] = 'alive'
			else:
				print "%r lost - we checked" % item[0] #debugging
				# Write 'dead' to this user's status - status is column[2]
				raw_people[dex][2] = 'dead'
		else: # If the user's status is 'dead' then check six picks column[3] thru column[8]
			if item[3] in clean_winners:
				if item[4] in clean_winners:
					if item[5] in clean_winners:
						if item[6] in clean_winners:
							if item[7] in clean_winners:
								if item[8] in clean_winners:
									print "%r passed - we checked" % item[0] # debugging
									# Write 'alive' to this user's status - status in column[2]
									raw_people[dex][2] = 'alive'
			else:
				print "%r lost - we checked" % item[0] # debugging
				# Write 'dead' to this user's status - status is column[2]
				raw_people[dex][2] = 'dead'
	print "Finished checking picks and setting statuses."

	print "Attempting to write the status of each user to the database"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	# Writing correct status to 'knockout.csv'
	with open('knockout.csv', 'wb') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(raw_people)
		fp.close()
		print "Successfully wrote dead or alive to each user."

# set_status_day3()

# Function to add user's picks on March 27th or after (1 and done)
def get_final_rounds_picks():
	# Get email address so that the picks are added to the right user
	cross_check_email = raw_input("Enter the email address you used to make your Knockout account: ")
	
	# Make a new list that will hold the users email addresses so we can crosscheck
	email_holder = []

	# Make a new list that will hold the users email addresses so we can crosscheck
	file1 = csv.reader(open('knockout.csv', 'rU'))
		
	# Place each row and column into raw_people
	raw_people = [l for l in file1]

	# Add the email address to the email_holder
	for item in raw_people:
		email_holder.append(item[1])

	# # Check all the emails for the address the user gave us to crosscheck
	# for address in email_holder:
		
	# If there is a match add the list of picks, 'new_picks', to users list_of_picks
	if cross_check_email in email_holder:
		dex = email_holder.index(cross_check_email)
		# Make sure dex is correct
		# print dex

		pick1 = raw_input("Enter your pick: ")			
		# Check to make sure pick1 is legal
		check_pick1(pick1)
				
		# Add the picks to the raw_people
		print "We found your account and are adding your picks"
		raw_people[dex][3] = pick1

		# Write the raw_people to knockout.csv
		with open('knockout.csv', 'ab') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerow(raw_people)
			fp.close()
			print "Your picks have been added. Good luck!"
		
	# If there is not a match, then prompt the user to enter another email
	else:
		print "We did not find the email you gave us, try entering another email address."
		get_final_rounds_picks()

# Calling function to add user's picks on March 27th or after (1 and done)
# get_final_rounds_picks()

def set_status_final_rounds():
	file1 = csv.reader(open('knockout.csv', "rU")) # Opening 'knockout.csv' and setting to file1
	file2 = csv.reader(open('list_of_winners.csv', "rU")) # Opening 'list_of_winners.csv' and setting to file2

	raw_people = [l for l in file1]
	raw_winners = [l for l in file2]
	clean_winners = []


	print "Here are the users first picks:" # Debugging
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
	for item in raw_people:
		dex = raw_people.index(item)
		print "%s's first pick is: %s" % (raw_people[dex][0], raw_people[dex][3])

	print "Here are the users second picks:" # Debugging
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	for item in raw_people:
		dex = raw_people.index(item)
		print "%s's second pick is: %s" % (raw_people[dex][0], raw_people[dex][4])

	print raw_winners # debugging

	print "Here are the list of winners:" # Debugging
	for item in raw_winners:
		dex = raw_winners.index(item)
		print "%s" % raw_winners[dex][0]
		clean_winners.append(raw_winners[dex][0])

	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	print "Here's who passed the round:"
	for item in raw_people:
		dex = raw_people.index(item)
		status = raw_people[dex][2]
		print "%s's status before checking is: %s" % (raw_people[dex][0], status) # debugging

		if status == 'alive': # Check to see user's status, if 'alive', only check one pick - column[3]
			if item[3] in clean_winners: # index of the first pick
				print "%r passed - we checked" % item[0] # debugging
				# Write 'alive' to this user's status - status is column[2]
				raw_people[dex][2] = 'alive'
			else:
				print "%r lost - we checked. You've been knocked out!" % item[0] #debugging
				# Write 'dead' to this user's status - status is column[2]
				raw_people[dex][2] = 'dead'
		else:
			print "%r lost - we checked. You've been knocked out!" % item[0] # debugging
			# Write 'dead' to this user's status - status is column[2]
			raw_people[dex][2] = 'dead'
	print "Finished checking picks and setting statuses."

	print "Attempting to write the status of each user to the database"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	# Writing correct status to 'knockout.csv'
	with open('knockout.csv', 'wb') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(raw_people)
		fp.close()
		print "Successfully wrote dead or alive to each user."

# set_status_final_rounds()

# After a day of games, place all the user's current_picks (columns[3] thru columns[8]) into old_picks
def scrub_current_picks():
	try:
		file1 = csv.reader(open('knockout.csv', "rU"))
		print "try hit"
	except:
		print "Could not open knockout.csv file."
		print "Ending program"
		raw_input("\n\nPress the enter key to exit.")
	else:
		print "else hit"
		raw_people = [l for l in file1] # Make a list of the columns and rows
		
		for item in raw_people:
			print "Name: %s" % item[0]
			old_picks = []
			dex = raw_people.index(item)
			old_picks.append([raw_people[dex][3],raw_people[dex][4],raw_people[dex][5],raw_people[dex][6],raw_people[dex][7],raw_people[dex][8]])
			print "Picks: %r" % old_picks
			raw_people[dex][9] = [old_picks]

		with open('knockout.csv', 'wb') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerows(raw_people)
			fp.close()
			print "Successfully moved users current picks to Old Picks column - column[9]"
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

		print "Starting process to update all current picks to 'empty' now."		
		
		for item in raw_people:
			dex = raw_people.index(item)
			raw_people[dex][3] = 'empty'
			raw_people[dex][4] = 'empty'
			raw_people[dex][5] = 'empty'
			raw_people[dex][6] = 'empty'
			raw_people[dex][7] = 'empty'
			raw_people[dex][8] = 'empty'

		print "Finished process to update all current picks to 'empty'."

		with open('knockout.csv', 'wb') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerows(raw_people)
			fp.close()
			print "Successfully cleared all current picks and are now set to 'empty'"

# scrub_current_picks()

