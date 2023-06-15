


class Protected:
    def __init__(self):
        self._proVar = 100 # This variable is protected, as denoted by "_"
        self.__priVar = 25 # This variable is private, as denoted by "__"

    def getPrivate(self):
        print(self.__priVar)

    def setPrivate(self, variable):
        self.__priVar = variable


Object = Protected()
print(Object._proVar)
Object.getPrivate()

