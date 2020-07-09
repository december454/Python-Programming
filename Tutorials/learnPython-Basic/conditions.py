# Python evaluates conditions using boolean variables, true and false. When an expression is compared or evaluated, either true or false is returned.

# Example
x = 4
print("X is equal to 2:", x == 2)
print("X is equal to 4:", x == 4)
print("X is greater than 3:", x > 3)

# You can assign variables using a single equal sign '='. Comparison between variables is done using two equal signs '=='. The 'not equals' operator is an equal sign proceeded by an exclamation point '!='.

# Example
x = 4
print("\nX is equals 2:", x == 2)
print("X does not equal 2:", x != 2)
print()

# Boolean Operators: You can build complex boolean expressions using the 'and' & 'or' operators.
name = "Jim"
age = 29

# If true, these statements will be printed.
if name == "Jim" and age == 29:
    print("Your name is Jim, and you are 29 years old.")

if name == "Jim" or name == "Julian":
    print("Your name is either Jim or Julian.")

# You can use the 'in' operator to check if a variable is found within an iterable object container (list).
num = 23
numList = [21,22,23,24,25]
name = "Jim"
nameList = ["Ricky", "Julian", "Jim", "Bubbles"]
print( )

# If true, these statements will be printed.
if num in numList:
    print("The number %d was in the list." %num)
if name in nameList:
    print("The name %s was in the list." %name)

# Instead of brackets, Python uses indentation to define code blocks. the default indentation is four spaces, but any indentation will work as long as it's consistant.
statement1 = False
statement2 = True
if statement1 is True:
    # do stuff
    pass
elif statement2 is True: #Else if statement.
    # do more stuff
    pass
else:
    # do this if all else fails
    pass

x = 4
if x == 2:
    print("x equals two!")
else:
    print("x does not equal two.")

# A statement is evaluated as true if: 1. The 'true' boolean value is given. 2. An object which isn't considered empty is given.
# Empty objects: An empty string "", an empty list [], the number zero '0', the false booalean variable.
if 0 or [] or "" or False:
    print("These evaluate as true.")
else:
    print("These are empty.")

# The 'is' Operator: The double equals '==' operator compares the values of variables. The 'is' operator compares the variables themselves.
xList = [4,5,6,7]
yList = [4,5,6,7]
print("\nxList == yList : %s" %(xList == yList))
print("xList is yList : %s" %(xList is yList))

# The 'not' Operator: Putting 'not' before a boolean expression inverts it.
print ("\nnot false:", not False)
print ("not true:", not True)
