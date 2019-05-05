#
# Python: 3.6.6
#
# Author: Jan Masangcay
#
# Purpose: Creating a small program using Python.
#          Demonstrating how to pass variables from function to function
#          while producing a functional game
#
#          Remember, functionName(variable) _means that we pass in the variable.
#          return variable _means that we are returning the variable back to
#          the calling function.

def start(nice=0, mean=0, name=""):
    # get user's name
    name = getName(name)

def getName(userName):
    if userName != "":
        print('\nThank you for playing again, {}!'.format(userName))
    else:
        go = True
        while (go):
            userName = input('\nWhat is your name?\n>>>').capitalize()
            if userName != "":
                print('\nWelcome, {}.'.format(userName))
                print('\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean')
                print('but at the end of the game your fate \nwill be sealed by your actions.')
                go = False
    return userName   



if __name__ == "__main__":
    start()
