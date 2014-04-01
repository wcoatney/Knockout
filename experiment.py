import csv

def set_dead_or_alive():
	try:
		file1 = csv.reader(open('knockout.csv', "rU"))
	except:
		print "Could not open knockout.csv file."
		print "Ending program"
		raw_input("\n\nPress the enter key to exit.")
	else:
		columns1 = zip(*file1)
		name = columns1[0]
		email = columns1[1]
		status = columns1[2]
		pick1 = columns1[3]
		pick2 = columns1[4]

	try:
		file2 = csv.reader(open('list_of_winners.csv', "rU"))
	except:
		print "Could not open list_of_winners.csv file."
		print "Ending program"
		raw_input("\n\nPress the enter key to exit.")
	else:
		columns2 = zip(*file2)
		winners = columns2[0]

	print "Here are the users first pick:"
	for item in pick1:
		print item

	print "Here are the users second picks:"
	for item in pick2:
		print item

	print "Here are the list of winners:"	
	for item in winners:
		print item

	print "Here's who passed the first round:"
	
	try:
		file3 = csv.reader(open('knockout.csv', "rU"))
		file2 = csv.reader(open('list_of_winners.csv', "rU"))
	except:
		print "Could not open knockout.csv file."
		print "Ending program"
		raw_input("\n\nPress the enter key to exit.")
	else:
		raw_people = [l for l in file3]

		columns1 = zip(*file2)
		picks = columns1[0]
		
		for item in raw_people:
			if item[3] in picks: # index of the first pick
				if item[4] in picks: # index of the second pick
					print "%r passed" % item[0] # debugging
					# Write 'alive' to this user's status - status is column[2]
					dex = raw_people.index(item)
					raw_people[dex][2] = 'alive'
				else:
					print "%r lost" % item[0] #debugging
					# Write 'alive' to this user's status - status is column[2]
					dex = raw_people.index(item)
					raw_people[dex][2] = 'dead'
			else:
				print "%r lost" % item[0] #debugging
				# Write 'alive' to this user's status - status is column[2]
				dex = raw_people.index(item)
				raw_people[dex][2] = 'dead'

		print "Attempting to set the status of each user"
		print "~~~~~~~~~~~~~"

		with open('knockout.csv', 'wb') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerows(raw_people)
			fp.close()
			print "Successfully wrote dead or alive to each user."

set_dead_or_alive()