# -- coding: utf-8 --
print "Hello World!"
print "Now I will do maths in python"
print 45 * 2
# Check if 4 is greater then 5
print 4 > 5
# Check if 4 is less then 5
print 4 < 5
print 4 % 3

print float(4.2 + 2.4)


# Now lets start playing with variables
fruits = 5
vegetables = 6
total = fruits + vegetables
mashedStuf = fruits * vegetables
print total
print "meshed stuff is", mashedStuf

# Lets talk about variable replacement
name = "Ashwani Solanki"
height = 6  # Feet
eyes_color = "Black"
hair_color = "Black"
age = 26
print "My Name is %s" % name
# %d is the qualifier for numbers, %s qualifier for strings. 
# I can use string's qualifier (%s) for numbers but can't use number qualifier for strings. For obvious type conversion reasons.
print "Iam %d feet tall" % height
print "My eyes are %s and hair are %s" % (eyes_color, hair_color)
print "Adding my height i.e. %d and age i.e. %d, I get %d" % (height, age, height + age)
# Lets check %r qualifier. This is great. Let it be string or number everything gets printed.
print "Checking %r" % height
