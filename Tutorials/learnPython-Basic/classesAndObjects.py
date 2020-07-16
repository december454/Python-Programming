# Objects encapsulate variables and functions into a single entity. Objects get their functions and cariables from classes. Classes act as a template to create objects.

# A simple class.
class testClass:
    testVar = "This is some text."

    def testFunc(sentVar):
        print ("This message is being sent from the class.")

# Assigning the class to an object.
testObject = testClass()

# Accessing Object Variables: Use the 'object.variable' format.
testObject.testVar
# Printing the variable within the object.
print (testObject.testVar)

# You can create multiple objects that are of the same class. They will each have independant conies of the functions and variables located within.

# Creating another object of the 'testClass'.
testObject2 = testClass()
# Modifying 'testObject2.testVar'.
testObject2.testVar = "This is some modified text."

# Printing out the 'testVar' from both objects.
print()
print (testObject.testVar)
print (testObject2.testVar)
print()

# Accessing Object Functions: You can access the functions inside of an object the same way you access variables. 'object.function()'
testObject.testFunc()
