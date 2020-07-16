# A dictionary is a data type, similar to an array. However, unlike arrays, you can identify an object using a custom 'key' instead of an index.

# Creating a dictionary of phonenumbers, used to identify each contact's name.

# Creating the 'phonebook'.
phonebook = {}
# Assigning a key (phone number) to each name.
phonebook ["Benson"] = 9792451616
phonebook ["Don"] = 9798452147
phonebook ["Eileen"] = 3614547891
phonebook ["Garrett"] = 2104578894
# Printing it out.
print (phonebook)
# Printing a normal array for comparison.
print (["Test String", "Another String", "Yet, another sting", "The last string"])
print()

# Like an array, you can initialize the dictionary and assign values all in one statement.
topSpeed = {
    "Blackbird" : 1996,
    "'Busa" : 1999,
    "ZX12r" : 2000,
    "ZX14" : 2006
}
# Printing out the dictionary entries.
print(topSpeed)

# Iterating Over Dictionaries: like arrays, you can iterate through dictionaries. However, a dictionary does not keep the order of its values.
# Use the 'dictionary.items()' format.
for bike, year in topSpeed.items():
    print("The %s was the fastest bike in %d." %(bike, year))
print()
# Printing out the phonebook.
for contact, number in phonebook.items():
    print("%s's phone number is %d." %(contact, number))
print()

# Removing a Value: Use either of the following notations to remove a specified index.
del phonebook["Garrett"]
print (phonebook)
# Alternate syntax.
topSpeed.pop("'Busa")
print (topSpeed)
