# String simply bits of text. They can be defined as anything between quotes.
aString = "Hello world!"
aString2 = 'Hello world!'

# In the first lesson, we printed out a simple sentence. Python stored that sentence as a string. Here we will learn how to further manipulate strings before printing them out.

# You can assign string using single quotes, but double quotes let you create strings that contain single quotes.
print("These are singel quotes ''''''")

# Printing out the lenth of a string, number of characters, using 'len()'.
print(len(aString))
print(len("a"))

# Printing out the index of the character 'o'. This will find the first occurrance of the character.
print("Index of 'o': ", aString.index("o"))
print("Index of 'l': ", aString.index("l"))

# This prints out a chunk of the string, from index 3 to 7.
print(aString[3:7])

# Printing out a chunk of the string. Fourth character from the end -> second from the end.
print(aString[-4:-2])
print("")

aString="123456789"
print(aString[2:8])
# Printing the chunk from 2 to 8, skipping every other character. [start:stop:step]
print(aString[2:8:2])

# There is no dedicated function to print a string in reverse, but you can modify the prior operation to do this.
print(aString)
print(aString [::-1])
print()

# You can use the following operations to make a string all lowercase or uppercase.
aString2 = "Hello World"
print(aString2)
print(aString2.upper())
print(aString2.lower())
print()

# You can use the follwing boolean operation to see if a string begins or ends with some specified text.
aString2 = "Hello World!"
print(aString2.startswith("Hello"))
print(aString2.endswith("orld!"))
print(aString2.endswith("qwerty"))
print()

# You can use this operation to split up a string into a list. This example will break up the string at each dash.
aString2 = "Hello-there-every-body!"
print(aString2.split("-"))