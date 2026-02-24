class Car():
    def __init__(self, name, manufacturer, color, year, cc):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.cc = cc
        
    def start(self):
        print("Starting the engine.")
    def brake(self):
        print("Applying the brakes.")
    def drive(self):
        print("Driving the car.")
    def turn(self, direction):
        print("Turning", direction)
    def change_gear(self, gear):
        print("Changing to gear", gear)

my_car = Car("IDK", 'BMW', 'Black', 2020, 2000)
my_car2 = Car("IDK2", 'Mercedes', 'White', 2021, 2500)
print(my_car.name,
      my_car.manufacturer,
      my_car.color,
      my_car.year,
      my_car.cc)
print(my_car2.name,
      my_car2.manufacturer,
      my_car2.color,
      my_car2.year,
      my_car2.cc)
my_car.start()
my_car.drive()
my_car.turn("Right")
my_car.change_gear(2)
my_car.brake()