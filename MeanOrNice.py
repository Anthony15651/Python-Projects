#
# Python:   3.11.1
#
# Author:   Anthony Garcia
#
# Purpose:  Creating a functioning game using Python by
#           following the instruction of The Tech Academy,
#           and then disecting the code to gain a better
#           understanding of Python in general.
#

def start(nice = 0, mean = 0, name = ''):
    # Get the user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """ Check if this is a new game or not. If it is new, get
    the user's name. If it is NOT new, thank the player for
    playing again and continue with the game. """
    if name != '':
        print('\nThank you for playing again, {}!'.format(name))
    else:
        stop = True
        while stop:
            if name == '':
                name = input('\nWhat is your name?\n>>>:').capitalize()
                if name != '':
                    print('\nWelcome, {}!'.format(name))
                    print('\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean,')
                    print('but at the end of the game your fate \nwill be sealed by your actions.')
                    stop = False
    return name

def nice_mean(nice,mean,name):
    """ Scenario #1 """
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nA stranger approaches your for a conversation. \nWill you be nice or mean? (N/M) \n>>>: ').lower()
        if pick == 'n':
            print('\nThe stranger walks away smiling...')
            nice += 1
            stop = False
        if pick == 'm':
            print('\nThe stranger glares at you \nmenacingly and storms off...')
            mean += 1
            stop = False
    score(nice,mean,name) # Passes the 3 variables to the score()











if __name__ == "__main__":
    start()
