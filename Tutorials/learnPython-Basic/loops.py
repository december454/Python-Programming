# Python featues two types of loops: 'for' loops and 'while' loops.

# The 'for' Loop: For loops iterate over a specified sequence.
print ("Example: 'for' loop")
numList = [1,2,3,4,5]
for num in numList:
    print(num, end = ' ')

# For can interate of over a specific range of numbers using the 'range' & 'xrange' functions. Range returns a new list with numbers. Xrange returns an iterator (more efficient.) In Python 3, range now works the same as python 2's xrange.

# Prints out 0 - 4 (Starting at 0, not 1)
print("\n\nExample: 'range' function")
for x in range(5):
    print(x, end = ' ')

# Prints out 5 - 9
print()
for x in range (5, 10):
    print(x, end = ' ')

# Prints out 5,7,9,11 (5 - 11 skipping every other number)
print()
for x in range(5,12,2):
    print(x, end = ' ')

# The 'while' Loop: While loops repeat as long as a boolean condition is med.
count = 0
print("\n\nExample: 'while' loop")
while count < 5:
    print(count, end = ' ')
    count += 1 # Incrementing the variable.

# The 'break and 'continue' Statements: You can use 'break' to exit a loop, and 'continue' will make the loop go to the next cycle.
# Example: 'break'
print("\n\nExample: 'break'")
count = 0
while True: # Infinite loop
    print (count, end = ' ')
    count += 1 # Incrementing the variable
    # If count is greater than or equal to 5.
    if count >= 5:
        # Breaking out of the loop.
        break
# Example: 'continue'
print("\nExample: 'continue'")
for x in range (10):
    # If x is an odd number.
    if x % 2 == 1:
        # Running the loop again, skipping what's left.
        continue
    # Only printing even numbers.
    print (x, end = ' ')

# Using an 'else' Clause with Loops: Unlike many other programming languages, Python lets you use else statements with loops. Whenever the loop condition fails the else statement is executed.
print ("\n\nExample: else statements")
count = 0
while (count < 4):
    print (count, end = ' ')
    count += 1
# Else statement activated after loop fails.
else:
    print ("\nThe count reached %d." %count)

# The else is not activated when the loop fails via a 'break'.
for i in range (1,10):
    if (i % 5 == 0):
        break
    print (i, end = ' ')
else:
    print ("This else was activated.")