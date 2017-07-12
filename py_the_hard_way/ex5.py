name =  "rae"
age = 28 # not a lie
height_in = 61 # inches
height_cm = height_in * 2.54 # cm
weight_lbs = 120 # lbs
weight_kg = weight_lbs * 0.453592
eyes = "blue"
hair = "brown"
teeth = "white"

print "Let's talk about %r." % name
print "They're %d inches tall or %r centimeters tall." % (height_in, height_cm)
print "They weigh %d pounds or %g kilograms." % (weight_lbs, weight_kg)
print "They've got %s eyes and %s hair." % (eyes, hair)
print "Their teeth are usually %s depending on coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height_in, weight_lbs, age + height_in + weight_lbs)
