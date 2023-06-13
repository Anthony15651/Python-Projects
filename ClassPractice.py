

class Vehicle: #Creating a parent class
    engineType = 'Gasoline'
    physicalForm = 'Coupe'
    numberOfDoors = '2'
    accelerationMethod = 'Gas Pedal'
    decelerationMethod = 'Brake Pedal'

class Car(Vehicle):#Creating a child class
    numberOfWheels = 4
    trunkSpace = '4 Cubic Feet'

class Helicopter(Vehicle):#Creating a child class
    numberOfRotors = 4
    maxLiftCapacity = '4000 lbs'
