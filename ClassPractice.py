

class Vehicle:
    engineType = 'Gasoline'
    physicalForm = 'Coupe'
    numberOfDoors = '2'
    accelerationMethod = 'Gas Pedal'
    decelerationMethod = 'Brake Pedal'

class Car(Vehicle):
    numberOfWheels = 4
    trunkSpace = '4 Cubic Feet'

class Helicopter(Vehicle):
    numberOfRotors = 4
    maxLiftCapacity = '4000 lbs'
    
