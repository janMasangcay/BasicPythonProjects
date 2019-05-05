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
    nice, mean, name = niceMean(nice, mean, name)

def getName(userName):
    """
        Check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
    """
    # meaning, if we do not already have this user's name,
    # then they are a new player and need to get their name
    if userName != "":
        print('\nThank you for playing again, {}!'.format(userName))
    else:
        go = True
        while go:
            userName = input('\nWhat is your name?\n>>>').capitalize()
            if userName != "":
                print('\nWelcome, {}.'.format(userName))
                print('\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean')
                print('but at the end of the game your fate \nwill be sealed by your actions.')
                go = False
    return userName   

def niceMean(nice, mean, userName):
    go = True
    while go:
        showScore(nice, mean, userName)
        pick = input('\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>').lower()
        if pick == 'n':
            print('\nThe stranger walks away smiling...')
            nice = nice + 1
            go = False
        if pick == 'm':
            print('\nThe stranger glares at you \nmenacingly and storms off...')
            mean = mean + 1
            go = False
    score(nice, mean, userName) # pass the 3 variables to the score()
    return nice, mean, userName

def showScore(nice, mean, userName):
    print('\n{}, your current total: \n(Nice: {}) and (Mean: {})'.format(userName, nice, mean))

def score(nice, mean, userName):
    # score function is being passed the value stored within the 3 variables
    if nice > 2: # if condition is valid, call win() passing in the variables so it can use them
        win(nice, mean, userName)
    elif mean > 2: # if condition is valid, call lose() passing in the variables so it can use them
        lose(nice, mean, userName)
    else:        # else, call niceMean() passing in the variables so it can use them
        niceMean(nice, mean, userName)

def win(nice, mean, userName):
    # Substitute the {} wildcards with our variable values
    print('\nNice job {}, you win! \nEveryone loves you and you\'ve \nmade lots of friends along the way!'.format(userName))
    # call again() and pass in our variables
    again(nice, mean, userName)

def lose(nice, mean, userName):
    # Substitute the {} wildcards with our variable values
    print('\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!'.format(userName))
    # call again() and pass in our variables
    again(nice, mean, userName)

def again(nice, mean, userName):
    go = True
    while go:
        playAgain = input('\nDo you wanna play again? (y/n):\n>>>').lower()
        if playAgain == 'y':
            go = False
            reset(nice, mean, userName)
        elif playAgain == 'n':
            print('\nOh, so sad, sorry to see you go!')
            go = False
            quit()
        else:
            print('\nEnter ( Y ) for "YES", ( N ) for "NO": \n>>>')
        
def reset(nice, mean, userName):
    nice = 0
    mean = 0
    # userName is being passed back, this changes the flow of getName()
    start(nice, mean, userName)




if __name__ == "__main__":
    start()
