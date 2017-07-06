import random

roll_time = raw_input("How many times would you like to roll the dice? > ")
x_times = int(roll_time)
# print(type(x_times))

print ("Let's roll!")
print ("*-------------*")

for x in range(x_times):
    y = random.randint(1, 6)
    z = random.randint(1, 6)
    print (y, z)

print ("*-------------*")
print ("Dice rolled " + roll_time + " times")
print (" <<< script complete >>>")
