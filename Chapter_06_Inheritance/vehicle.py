class Vehicle:
    """Base class for all vehicles"""
    def __init__(self, name, manufacturer,color):
        self.name = name
        self.color = color
        self.manufacturer = manufacturer
    
    def drive(self):
        print("Driving", self.manufacturer, self.name)
    
    def turn(self, direction):
        print("Turning", self.name , "to", direction)
    
    def brake(self):
        print(self.name, "is stopping!")

class Car(Vehicle):
    """Car class"""
    def __init__(self, name, manufacturer, color, year):
        super().__init__(name, manufacturer, color)
        self.year = 2017
        self.wheels = 4
        print("A new car has been created. Name:", self.name)
        print("It has", self.wheels, " wheels")
        print("The car was built in", self.year)

    def change_gear(self, gear_name):
        """Method for changing gear"""
        print(self.name, "is changing gear to", gear_name)
    
    def turn(self, direction):
        print(self.name, "is turning", direction)

class Motorcycle(Vehicle):
    """Motorcycle class"""
    def __init__(self, name, manufacturer, color, year, wheels, cc):
        super().__init__(name, manufacturer, color)
        self.year = year
        self.wheels = wheels
        self.cc = cc
        print("A new motorcycle has been created. Name:", self.name)
        print("It has", self.wheels, " wheels")
        print("The motorcycle was built in", self.year)
    def turn(self, direction):
        print(self.name, "is leaning to the", direction)

if __name__ == "__main__":
    v1 = Vehicle("Fusion 110 EX", "Walton", "Black")
    v2 = Vehicle("Softail Delux", "Harley-Davidson", "Blue")
    v3 = Vehicle("Mustang 5.0 GT Coupe", "Ford", "Red")
    
    v1.drive()
    v2.drive()
    v3.drive()
    
    v1.turn("left")
    v2.turn("right")
    
    v1.brake()
    v2.brake()
    v3.brake()
    
    c = Car("Mustang 5.0 GT Coupe", "Ford", "Red", 2017)
    c.drive()
    c.change_gear("P")
    
    v1.turn("left")
    c.turn("right")
    
    m = Motorcycle("Softail Delux", "Harley-Davidson", "Blue", 2018, 2, 1746)
    m.drive()
    m.turn("left")