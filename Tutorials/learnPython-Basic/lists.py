# Lists are similar to arrays. They can contain any type of variable and as many variables as you like.
# Lists can be interated quite easily.

# Creating a List. List denoted with square brackets.
myList = []
# Adding items to the list with '.append()"
myList.append(4)
myList.append(5)
myList.append(6)

# Printing values from the list. Refer to values using the list's name followed by '[index]'
print (myList [0], myList [1], myList [2])

# You can also assign multiple values to a list with one statement. Enclose multiple values in the square braces, separated with commas.
myList = [7,8,9]

# Simple for each loop that prints out each of the values in the list.
for x in myList:
    print(x)

# Trying to access an index that doesn't exist will throw an error.

#This would throw an error.
# print(myList[420])