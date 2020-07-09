# Exercise
# Change the variables in the first section, so that each if statement resolves as True.

# change this code
number = 16
second_number = 0
first_array = [1, "a", "b"]
second_array = [1,2]

# If the 'number' is greater than 15.
if number > 15:
    print("1")

# If the first array is not empty.
if first_array:
    print("2")

# If tthe 'second_array' has a length of 2.
if len(second_array) == 2:
    print("3")

# If the length of 'first_array' + the length of 'second_array' is 5.
if len(first_array) + len(second_array) == 5:
    print("4")

# If 'first_array' is not empty and 'first_array[0]' is 1.
if first_array and first_array[0] == 1:
    print("5")

# If 'second_number' is not not empty.s
if not second_number:
    print("6")