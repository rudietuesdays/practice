# exercise 11

# input() reads a value from standard input as a Python expression
# raw_input() reads a string from standard input and trailing newline is stripped

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r years old, %r tall and %r heavy." % (age, height, weight)

print "Enter an integer:",
num = int(raw_input())
print "The number you input is %d." % num

print "Enter a name:",
name = raw_input()
print "What's %s's age?" % name,
age = input()
print "What's %s's height?" % name,
height = input()
print "What's %s's weight?" % name,
weight = input()
print "What color are %s's eyes?" % name,
eyes = raw_input()
print "What color are %s's teeth?" % name,
teeth = raw_input()
print "What color is %s's hair?" % name,
hair = raw_input()

print type(name) # string
print type(age) # int

print "Let's talk about %s." % name
print "She's %d years old." % age
print "She's %d inches tall." % height
print "She weighs %d pounds." % weight
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s, depending on coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
