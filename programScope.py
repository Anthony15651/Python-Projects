


name = "Python"

def getName():
    name = "C#"
    print("I am coding with {}".format(name))

getName()

print('And that is a \nBOLD FACED LIE')

print('I\'m actually coding with ' + name)


def getName():
    fName = input('What is your first name? ').lower()
    lName = input('What is your last name? ').lower()
    if fName == 'anthony' and lName == 'garcia':
         print('Welcome back to your computer, Anthony.')
    else:
         print('Hello {} {}, welcome to Anthony\'s computer!'.format(fName.capitalize(),lName.capitalize()))
    getName()


getName()
