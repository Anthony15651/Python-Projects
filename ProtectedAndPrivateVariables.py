


# Here is an example of a protected variable, denoted by a single "_"
class Protected:
    def __init__(self):
        self._proVar = 100

Object1 = Protected()
print(Object1._proVar)
Object1._proVar = 50
print(Object1._proVar)


# Here is an example of a private variable, denoted by two "_"
class Private:
    def __init__(self): # Initializes variable
        self.__priVar = 25
        
    def getPrivate(self): # Prints current variable
        print(self.__priVar)

    def setPrivate(self, variable): # Sets a new variable
        self.__priVar = variable

Object2 = Private()
Object2.getPrivate()
Object2.setPrivate(0)
Object2.getPrivate()
