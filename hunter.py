# import csv

# winner_file = csv.reader(open('list_of_winners.csv', "rU"))

# raw_winners = [l for l in winner_file]
# winner_list = []

# for item in raw_winners:
#    winner_list.append(item[0])

# people_file = csv.reader(open('knockout.csv', "rU"))

# raw_people = [l for l in people_file]

# for item in raw_people:
#    # print item[6] # debugging
#    # print item[7] # debugging
#    # print "~~" # debugging
#    if item[6] in winner_list: # index of the first pick
#       if item[7] in winner_list: # index of the second pick
#          print "%r won" % item[0] # debugging
#       else:
#          print "%r lost" % item[0] #debugging
#    else:
#       print "%r lost" % item[0] #debugging


myList = ["hello", "monkey", "flargan"]

if "meow" in myList:
   print "Meow it is"
elif "hello" in myList:
   print "Hellooo"

else: 
   print "I hate you"

print myList


