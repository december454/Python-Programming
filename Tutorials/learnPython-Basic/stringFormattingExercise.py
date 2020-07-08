# You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
# Placing arguments in the string for each index of the list.
format_string = "Hello %s %s. Your current balance is $%s."

# Printing out the string with the inserted values.
print(format_string % data)