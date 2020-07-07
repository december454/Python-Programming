# Every variable in Python is an object.
# You do not need to decalre variables before you use them.
# You do not need to declare a variable's type.

# Numbers - Python features two types of numbers: Integers & Floating Point Numbers

# To define an Integer:
myInt = 3

# To define a Floating Point variable:
myFloat = 3.0       #Notation one
myFloat = float(3)  #Notation two

print (myInt)
print (myFloat)

# Strings - String can be defined with single quotes or double quotes.

myString = 'hello'  #Notation one
myString = "hello"  #Notation two

print (myString)

# If you use double quotes, you can include apostrophes in the string itself.
myString = "This string contains 'apostrophes'"

print (myString)

# There are simple operators that can be executed on numbers and strings.
twelve = 12
three = 3

# Addition
addition = twelve + three
# Subtraction
subtraction = twelve - three
# Multiplication
multiplication = twelve * three
# Division
division = twelve / three

print ("12 + 3 = ", addition, "\n12 - 3 = ", subtraction, "\n12 x 3 = ", multiplication, "\n12 / 3 = ", division)

#Combining strings
string1 = 'pyt'
string2 = 'hon'
string3 = string1 + string2

print (string3)

# You can assign multiple values to multiple variables with one statement.
a, b = 5, 6
print ("\na = ", a, "& b = ", b)

# You cannot mix operators with strings and numbers.
one = 1
two = 2
word = "word"
# This would cause and error:
# print (one + two + word)

















