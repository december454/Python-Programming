# Python uses C-style string formatting to create formatted strings. The '%' operator lets you format a set of avriables enclosed in a tuple (fixed size list) along with a format string (%s, %d, etc).

name = "Cody"
print("Hello, %s!" % name)

# To use multiple arguments, use a tuple (parenthesis).
name = "Victoria"
age = 32
# Variable names enclosed in parenthesis.
print("%s is %d years old." % (name, age))

# You can format any object using th '%s' operator, not just strings.
myList = [4,5,6,7]
print("A list: %s" % myList)
# Why not do it this way? Acheives the same thing.
print("A list:", myList)

# Here are some basic arguments to know:
# %s - String (Works for any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f -Floating point numbers with a fixed number of decimals. Example, %.2f truncates 2.34567 to 2.34.
num = 4.1252341
print ("Truncated %.3f" % num)
# %x - Integers in hexadecimal format. Use %X for upper case.
num = 142
print ("Hex: %X" %num)