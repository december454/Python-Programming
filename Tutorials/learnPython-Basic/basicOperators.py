# Arithmetic Operators: Like other progamming languages you can easily add, subtract, multiply, and divide within python.

# Using some basic operators.
number = 1 + 2 * 3 / 4.0
# Python follows the order of operations.
print("Basic operators:", number)

# Python also features the modulo '%' operator which returns the remainder.
number = 25 % 7
# 25 / 7 = 3 with a remainder of 4
print("Modulo:", number)

# Two multiplication symbols '**' denotes an exponent relationship.
squared = 7 ** 2
cubed = 4 ** 3
# 7^2 = 49 & 4^3 = 64
print("Squared", squared)
print("Cubed", cubed)

# Using Operators with Strings: You can concantonate strings with the addition '+' operator.

# Concantonating strings
string = "hi" + " " + "there"
print(string)

#You can also multiply string to repeat a string.
fiveWoahs = "Woah " * 5
print(fiveWoahs)

# Using Operators with Lists: You can join lists with the addition '+' operator.
twenties = [23,24,25,26]
thirties = [37,38,39]
allNumbers = twenties + thirties
print(allNumbers)

# Like strings, you can also use the multiplication '*' operator with lists.
print(["A","B","C"] * 2)