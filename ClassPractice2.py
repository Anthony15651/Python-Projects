

class Vehicle: #Creating a parent class
    engineType = 'Gasoline'
    physicalForm = 'Coupe'
    numberOfDoors = '2'
    accelerationMethod = 'Gas Pedal'
    decelerationMethod = 'Brake Pedal'
    speed = 0

    def accelerate(self):
        speed = 25
        return speed
        

class Car(Vehicle):#Creating a child class
    numberOfWheels = 4
    trunkSpace = '4 Cubic Feet'
    traction = 1

    def accelerate(self):
        speed = 50
        traction = .75
        return speed,traction

class Helicopter(Vehicle):#Creating a child class
    altitude = 0
    numberOfRotors = 4
    maxLiftCapacity = '4000 lbs'

    def accelerate(self): #Polymorphing the method
        speed = 100
        altitute = 1000
        return speed,altitute
    


if __name__ == '__main__':
    vehicle1 = Vehicle()
    print(vehicle1.accelerate())

    car1 = Car()
    print(car1.accelerate())

    helicopter1 = Helicopter()
    print(helicopter1.accelerate())
