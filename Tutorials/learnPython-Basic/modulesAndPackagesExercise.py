## Exercise
# In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word find.

import re

# Your code goes here

# Creating a list to hold the function names that contain 'find'.
find_members = []

# A loop that will go through every function in 're'.
for func in dir (re):
    # If the function has 'find' ini ites name.
    if ("find" in func):
        # Adding that fucntion to the list.
        find_members.append (func)

# Alphabetizing the list.
list.sort(find_members)

# Printing the list.
print (find_members)