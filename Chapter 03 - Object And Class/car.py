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