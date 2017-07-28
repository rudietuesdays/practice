# exercise 13

from sys import argv

# print argv

script = argv(0)

txt = open (script)

print txt.read()

txt.close()

# script, first_name, last_name = argv
#
# print "The scrips is called: ", script
# print "Your first name is:", first_name
# print "Your last name is:", last_name
