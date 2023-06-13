

# Parent Class
class Organism:
    name = 'Unknown'
    species = 'Unknown'
    legs = None
    arms = None
    dna = 'Sequence A'
    origin = 'Unknown'
    carbonBased = True

    def information(self):
        msg = '\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}'\
              .format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbonBased)
        return msg

# Child Class
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = '\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!'
        return msg

# Another Child Class
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = 'Sequence B'
    origin = 'Earth'

    def bite(self):
        msg = '\nEmits a loud, menacing growl and bites down ferociously on it\'s target!'
        return msg

# Another Child Class
class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = 'Sequence C'
    origin = 'Mars'

    def replication(self):
        msg = '\nThe cell begins to divide into two separate organisms!'
        return msg


if __name__ == '__main__':
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
    
