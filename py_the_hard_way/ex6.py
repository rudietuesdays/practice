x = "There are %d types of people." % 10 # uses a formatter for integers
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # uses the formatter for strings

print x
print y

print "I said: %r" % x # %r uses a raw formatter; best for debugging
print "I also said: '%s'" % y

hilarious = False
joke_evaluation = "Isn't that joke funny? %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a ride side."

print w + e
