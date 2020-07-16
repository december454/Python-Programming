# Functions let you divde your code into useful blocks. Functions can make your code more readible and allow your to reuse code within your program.
# You follow the same indentation rules when defining functions.
# Functions are defined using the keyword 'def' followed by the function's name.
def testFunc():
    print ("This is being printed by the function\n")

# You then call to the function using its name, followed by parenthesis.
testFunc()

# Functions can also be sent arguments whenever they are called. You enter the arguments into the paranthese following the name of the function when it is called.
def sendFunc(name, age):
    print ("Your name is %s, and you are %d years old\n" %(name, age))
# Sending the variables.
sendFunc ("Andrew", 35)

# How Do You Call Functions in Python: You type the function's name followed by '()'. Place any required variables in the parenthesis.

def basicFunc():
    print("No arguments were sent to this function.")

def numFunc(num1, num2):
    print("Two numbers were sent to this function: %d and %d." %(num1, num2))

def stringFunc(string1, string2):
    print("Two strings were sent to this function: '%s' and '%s'." %(string1, string2))

# Calling to the functions.
basicFunc()
# Calling to the functions and sending them arguments.
numFunc(42,3)
stringFunc("Hello", "There")

# Functions can also 'return' values to the caller.
def productFunc (num1, num2):
    # Using the 'return' keyword.
    return num1 * num2

def subFunc (num1, num2):
    return num1 - num2

# Calling to the functions, sending them values, and receiving a value back.
print ("\nValue returned from the product function:", productFunc(7,6))
print ("Value returned from the subtraction duntion:", subFunc(128,32))

