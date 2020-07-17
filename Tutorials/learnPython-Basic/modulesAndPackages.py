# In programming, a module is a piece of software that a has a specific function. For example, if you were making a racing game, you may have a module for the physics engine, the AI opponents, and a module for rendering the

## Writing Modules:
# In Python, modules are simply Python files with the '.py' extension. The modules will have the same name as the file. A Python module can contain functions, classes, variables, etc. In this example, the following files will be used:
# myGame/game.py
# myGame/draw.py

# The Python script 'game.py' will implement the game. It will use the 'draw_game' function from 'draw.py' (the 'draw' module).

# Modules are imported using the 'import' command. Make sure your shell is in the right directory.
import myGame.draw
import functions

functions.basicFunc()

def playGame():
    print ()

# def main():
#     result = playGame()
#     myGame.draw.drawGame()


# If the script is executed, then '__main__' will be executed.
# if __name__ == '__main__':
#     main()
# If we wanted to call the 'drawGame()' function within the 'draw.py' module, we would type 'draw.drawGame()'

## Exploring Built-in Modules
# Two functions can be very useful while exploring modules in Python - the 'dir' and 'help' functions.

# Importing a module.
import urllib
# Uing the 'dir' function
dir(urllib)
# Using the 'help' function.
help (urllib)

## Writing Packages
# Packages are namespaces wich contain multiple modules as well as other packages. They are simply directories.
# Each package is Python is a directory that MUST contain a file named 'init.py'. The file can be empty, but it must exist.

# You can import a package using either syntax:
# import testPackage.insidePackage
# testPackage.insidePackage.printTest()
# from testPackage import insidePackage
# insidePackage.printTest()
