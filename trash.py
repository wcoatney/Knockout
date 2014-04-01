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
