class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement the 'make_sound' method")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

def animal_sounds(animals):
    for animal in animals:
        print(f"{animal.name} says {animal.make_sound()}")

if __name__ == "__main__":
    animals = [Dog("Fido"), Cat("Whiskers"), Bird("Tweety")]
    animal_sounds(animals)