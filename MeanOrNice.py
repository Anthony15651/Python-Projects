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
    nice,mean,name = nice_mean0(nice,mean,name)

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

def nice_mean0(nice,mean,name,scenario = 0):
    """ Scenario #1: Stranger approaches for conversation """
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nA stranger approaches your for a conversation. \nWill you be nice or mean? (N/M) \n>>>: ').lower()
        if pick == 'n':
            print('\nThe stranger walks away smiling...')
            nice += 1
            scenario += 1
            stop = False
        if pick == 'm':
            print('\nThe stranger glares at you \nmenacingly and storms off...')
            mean += 1
            scenario += 1
            stop = False
    score(nice,mean,name,scenario) # Passes the 4 variables to the score()

def nice_mean1(nice,mean,name, scenario):
    """ Scenario #2: Stranger asks for a ride """
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nYou are driving down an empty highway and you \nsee a stranger walking alone trying to flag you down. \nWill you be nice or mean? (N/M) \n>>>: ').lower()
        if pick == 'n':
            print('\nYou give the grateful stranger a ride...')
            nice += 1
            scenario += 1
            stop = False
        if pick == 'm':
            print('\nYou leave the stranger stranded alone...')
            mean += 1
            scenario += 1
            stop = False
    score(nice,mean,name,scenario) # Passes the 4 variables to the score()

def nice_mean2(nice,mean,name, scenario):
    """ Scenario #3: Stranger needs a hand carrying stuff """
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nYou are walking down a city sidewalk and \nrun into a stranger holding a pile of books \nin both hands. He is struggling to open the \ndoor in front of him. \nWill you be nice or mean? (N/M) \n>>>: ').lower()
        if pick == 'n':
            print('\nThe stranger thanks you for helping him with the door...')
            nice += 1
            scenario += 1
            stop = False
        if pick == 'm':
            print('\nThe stranger notices you make eye contact but continue walking. \nHis books drop into the puddle below. He remembers your face...')
            mean += 1
            scenario += 1
            stop = False
    score(nice,mean,name,scenario) # Passes the 4 variables to the score()

def nice_mean3(nice,mean,name, scenario):
    """ Scenario #4: Stranger needs a place to sit """
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nYou are sitting on a crowded bus when an elderly \nstranger boards. There are no open seats. \nWill you be nice or mean? (N/M) \n>>>: ').lower()
        if pick == 'n':
            print('\nYou give the elderly stranger your seat. She gives \nyou an old butterscotch hard candy from her purse...')
            nice += 1
            scenario += 1
            stop = False
        if pick == 'm':
            print('\nYou hold your ground. The bus hits a bump and the \nelderly stranger falls, resulting in a broken hip...')
            mean += 1
            scenario += 1
            stop = False
    score(nice,mean,name,scenario) # Passes the 4 variables to the score()

def nice_mean4(nice,mean,name, scenario):
    """ Scenario #5: I run out of ideas """
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nThe creator of this game ran out \nof ideas for nice/mean situations. \nWill you be nice or mean? (N/M) \n>>>: ').lower()
        if pick == 'n':
            print('\nYou let the creator slide, he\'s worked hard enough...')
            nice += 1
            scenario += 1
            stop = False
        if pick == 'm':
            print('\nYou punish the creator and leave a negative review online...')
            mean += 1
            scenario += 1
            stop = False
    score(nice,mean,name,scenario) # Passes the 4 variables to the score()

def show_score(nice,mean,name):
    print('\n{}, your current total is: \n{} Nice\n{} Mean'.format(name,nice,mean))

def score(nice,mean,name,scenario):
    # The score() function is being passed values stored within the 3 variables above
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else: # Else calls nice_mean() to pass in the variables and use them
        if scenario == 1:
            nice_mean1(nice,mean,name,scenario)
        if scenario == 2:
            nice_mean2(nice,mean,name,scenario)
        if scenario == 3:
            nice_mean3(nice,mean,name,scenario)
        if scenario == 4:
            nice_mean4(nice,mean,name,scenario)
        # At this point, either "nice" or "mean" must be greater than 2, triggering the code above

def win(nice,mean,name):
    # If win condition is met, display winning sentence
    print('\nNice job {}, you win! \nEveryone loves you and you\'ve made lots of friends along the way!'.format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    # If loss condition is met, display losing sentence
    print('\nWell, {}, I hate to say it, but you are a terrible person. \nMaybe work on your people skills and try again.'.format(name))
    again(nice,mean,name)


def again(nice,mean,name):
    # This function is used to play the game again
    stop = True
    while stop:
        choice = input('\nDo you want to play again? (Y/N) \n>>>:').lower()
        if choice == 'y':
            stop = False
            reset (nice,mean,name)
        if choice == 'n':
            print('\nThat\'s too bad, I hope you had fun!')
            stop = False
            quit()
        else:
            print('\nPlease enter "Y" for "yes" or "N" for "no" \n>>>:')
            
def reset(nice,mean,name):
    nice = 0
    mean = 0
    # I am not reseting the "name" variable because the same user has asked to play again
    start(nice,mean,name)














            

if __name__ == "__main__":
    start()
