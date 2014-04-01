import csv

def get_day0_picks():
	# Get email address so that the picks are added to the right user
	cross_check_email = raw_input("Enter the email address you used to make your Knockout account: ")

	# Make a new list that will hold the users email addresses so we can crosscheck
	csv_holder = csv.reader(open('knockout.csv', 'rU'))
	raw_people = [l for l in csv_holder]
	email_holder = []
	for item in raw_people:
		email_holder.append(item[1])	

	# Make list of winners to check picks against
	csv_holder = csv.reader(open('list_of_winners.csv', 'rU'))
	raw_winners = [l for l in csv_holder]
	winners_holder = []
	for item in raw_winners:
		winners_holder.append(item[0])

	# Make list of old picks to check picks against
	old_picks_holder = []
	for item in raw_people:
		old_picks_holder.append(item[9])

	# # Check all the emails for the address the user gave us to crosscheck
	# for address in email_holder:
		
	# If there is a match add the list of picks, 'new_picks', to users list_of_picks
	if cross_check_email in email_holder:
		dex_checker = email_holder.index(cross_check_email)
		# Make sure dex_checker is correct
		print "%s index is %s: " % (raw_people[dex_checker][0],dex_checker)		
		
		# Get the first pick from the user
		pick1 = raw_input("Enter your first pick for the March 20th games: ")
		
		# Keep asking for pick1 until it is in winners_holder
		while pick1 not in winners_holder:
			pick1 = raw_input("Make sure you pick a team that's in the tourney: ")

		# Keep asking for pick1 until it is not in old_picks_holder
		
		# Get the second pick from the user
		pick2 = raw_input("Enter your second pick for the March 20th games: ")

		# Keep asking for pick1 until it is in winners_holder
		while pick2 not in winners_holder:
			pick2 = raw_input("Make sure you pick a team that's in the tourney: ")

		print "Pick number 1 for %s is: %s" % (raw_people[dex_checker][0],pick1)
		print "Pick number 2 for %s is: %s" % (raw_people[dex_checker][0],pick2)

		# Add the picks to the raw_people
		print "We found your account and are adding your picks"
		raw_people[dex_checker][3] = pick1
		raw_people[dex_checker][4] = pick2

		# Write the raw_people with pick1 and pick2 to knockout.csv
		with open('knockout.csv', 'wb') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerows(raw_people)
			fp.close()
			print "Your picks for the March 20th games have been added. Good luck!"
		
	# If there is not a match, then prompt the user to enter another email
	else:
		print "We did not find the email you gave us, try entering another email address."
		get_day0_picks()

# Calling function to add user's first 2 picks on Thursday, March 20th, 2014
# get_day0_picks()

def get_final_rounds_picks():
	# Get email address so that the picks are added to the right user
	cross_check_email = raw_input("Enter the email address you used to make your Knockout account: ")
	
	# Make a new list that will hold the users email addresses so we can crosscheck
	csv_holder = csv.reader(open('knockout.csv', 'rU'))
	raw_people = [l for l in csv_holder]
	email_holder = []
	for item in raw_people:
		email_holder.append(item[1])	

	# Make list of winners to check picks against
	csv_holder = csv.reader(open('list_of_winners.csv', 'rU'))
	raw_winners = [l for l in csv_holder]
	winners_holder = []
	for item in raw_winners:
		winners_holder.append(item[0])

	# Make list of old picks to check picks against
	old_picks_holder = []
	for item in raw_people:
		old_picks_holder.append(item[9])

	# # Check all the emails for the address the user gave us to crosscheck
	# for address in email_holder:
		
	# If there is a match add the list of picks, 'new_picks', to users list_of_picks
	if cross_check_email in email_holder:
		dex = email_holder.index(cross_check_email)
		# Make sure dex is correct
		# print dex

		status = raw_people[dex][2]
		
		print
		
		print "You can NOT pick any of your old picks, listed below (ignore the 'empty'):"
		for item in [old_picks_holder[dex]]:
			print item

		print
		
		print "Here are the list of games that you can choose a team from:\n"
		print "%s is playing %s" % (winners_holder[0], winners_holder[1])
		print "%s is playing %s" % (winners_holder[2], winners_holder[3])
		print "%s is playing %s" % (winners_holder[4], winners_holder[5])
		print "%s is playing %s" % (winners_holder[6], winners_holder[7])

		# Get the first pick from the user
		pick1 = raw_input("Enter your first pick: ")			
		# Keep asking for pick1 until it is in winners_holder
		while pick1 not in winners_holder:
			pick1 = raw_input("Make sure you pick a team that's in the tourney: ")
		# Keep asking for pick1 until it is not in old_picks_holder[dex]
		while pick1 in old_picks_holder[dex]:
			pick1 = raw_input("You've already used that team. Pick again: ")
		# Add the picks to the raw_people
		print "We found your account and are adding your picks\n"
		raw_people[dex][3] = pick1
			
		# Add the picks to the raw_people
		print
		print "We found your account and are adding your picks"
		raw_people[dex][3] = pick1

		# Write the raw_people to knockout.csv
		with open('knockout.csv', 'wb') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerows(raw_people)
			fp.close()
			print "Your picks for the March 27nd games have been added. Good luck!"
		
	# If there is not a match, then prompt the user to enter another email
	else:
		print "We did not find the email you gave us, try entering another email address."
		get_final_rounds_picks()