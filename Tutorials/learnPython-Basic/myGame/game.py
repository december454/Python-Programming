# game.py

import draw

def playGame():
    print("Do something.")

def main():
    result = playGame()
    draw.drawGame(result)

# If the script is executed, then 'main()' will be executed.

## Importing Module Objects to the Current Namespace
# You can import functions from a module directly, using 'from'.
# Importing a single function.
from draw import drawGame
# Importing all of the functions from a module, using the '*' wildcard.
from draw import *

# You do not need to type the module name before the function name if you import like this. However, you cannot have two functions with the same name if you use this method, it will overwite functions with the same name.

## Custom Import Name
# You can import a mondule using a name that you have specified.
import drawDifferent as draw
# Calling to a function in the module.
draw.customNameTest()

## Module Initialization
# Whenever a module is loaded for the virst time, it is initialized by executing its code once. If the module is inported again, it will not be intitialed again.

## Extending Module Load Path
# There are different ways to tell the Python interpreter where to look for modules, aside from the default. By default it will check the present working directory and the built-in modules.
# You can use the environmental variable 'PYTHONPATH' to specifiy additional locations.
# PYTHONPATH=/foo python game.py
# You can also use 'sys.path.append'.
# sys.path.append