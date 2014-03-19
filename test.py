import csv

def set_dead_or_alive():
	# Open knockout.csv and put into csv_holder
	csv_holder = csv.reader(open('knockout.csv', 'rU'))
	
	# Make a new list that will hold the users current_picks so we can crosscheck
	current_picks_holder = []

	# Place each row and column into file_loop
	file_loop_picks = [l for l in csv_holder]

	# Add the current_picks to the current_picks_holder
	for item in file_loop_picks:
		current_picks_holder.append(item[3])

	# Open list_of_winners.csv and put into winners_csv_holder
	winners_csv_holder = csv.reader(open('list_of_winners.csv', 'rU'))

	# Make a new list that will hold the list_of_winners so we can crosscheck
	winners_holder = []

	# Place each row and column into file_loop
	file_loop_winners = [l for l in winners_csv_holder]

	# Add the list_of_winners to the winners_holder
	for item in file_loop_winners:
		winners_holder.append(item[0])

	# See if the user's current picks are in the list_of_winners
	print "Here are the users current picks:"
	print current_picks_holder
	print "Here are the list of winners:"	
	print winners_holder

	# item is a list of the strings, or the picks
	for item in current_picks_holder:
		if all(x in item for x in winners_holder):
			print "Both picks won!"
			dex_checker = current_picks_holder.index(item)
			file_loop_picks[dex_checker][4] = 'alive'
			with open('knockout.csv', 'wb') as fp:
				a = csv.writer(fp, delimiter=',')
				a.writerows(file_loop_picks)
				fp.close()
				print "You're status has been set to ALIVE! You're moving on to the next round!"
		else:
			print "One or both of your picks lost..."
			dex_checker = current_picks_holder.index(item)
			file_loop_picks[dex_checker][4] = 'dead'
			with open('knockout.csv', 'wb') as fp:
				a = csv.writer(fp, delimiter=',')
				a.writerows(file_loop_picks)
				fp.close()
				print "You're status has been set to DEAD! Do you want to buy back into the tourney?"

			# if item[0] in winners_holder:
			# 	first_pick_val = 1
			# else:
			# 	first_pick_val = 0
			# if item[1] in winners_holder:
			# 	second_pick_val = 1
			# else:
			# 	second_pick_val = 0

			# if first_pick_val == 1 and second_pick_val == 1:
			# 	dex_checker = current_picks_holder.index(item)
			# 	file_loop_picks[dex_checker][4] = 'alive'
			# 	with open('knockout.csv', 'wb') as fp:
			# 		a = csv.writer(fp, delimiter=',')
			# 		a.writerows(file_loop_picks)
			# 		fp.close()
			# 		print "You're alive and moving to the next round!"
			# else:
			# 	with open('knockout.csv', 'wb') as fp:
			# 		a = csv.writer(fp, delimiter=',')
			# 		a.writerows(file_loop_picks)
			# 		fp.close()
			# 		print "You're dead... Do you want to buy back in?"



set_dead_or_alive()