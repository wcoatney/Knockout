import csv

# Check to make sure the users new picks have not been picked before
def check_past_picks:
	# Make a new list that will hold the users current_picks so we can crosscheck
	csv_holder = csv.reader(open('knockout.csv', 'rU'))
	picks_holder = [[]]
	file_loop = [l for l in csv_holder]

	# Iterate through each of the picks and append current_picks to picks_holder
	for item in file_loop:
		picks_holder.append(item[3])
	
	# Make sure that the user's new picks are not in old_picks
	if pick in picks_holder:
		print "You have already used that team for a pick. That's against the rules."