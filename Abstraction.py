
# Importing ABC
from abc import ABC, abstractmethod

# Parent Class
class myMath(ABC):
    def Add(self, num1, num2):
        result1 = num1 + num2
        print(result1)
    @abstractmethod
    def Multiply(self, num1, num2):
        pass

# Child Class
class Multiplication(myMath):
    def Multiply(self, num1, num2):
        result2 = num1 * num2
        print(result2)


Object = Multiplication()
Object.Add(5, 5) # Calling "Add()" from "Multiplication" because it is inherited
Object.Multiply(5, 5) # Calling "Multiply" from "Multiplication"
