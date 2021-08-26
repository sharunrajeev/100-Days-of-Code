# Inheritance
# Inheritance is a way to inherit the attributes and methods of another class.

# Parent class/ Super class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print(self.make, self.model, self.year)
    
# Child class/ Sub class (inherits from Vehicle class)
class Car(Vehicle):
    def __init__(self, make, model, year, seat_count):
        Vehicle.__init__(self, make, model, year)   # call the constructor of Vehicle class
        self.no_of_tyres = 4
        self.no_of_seats = seat_count

    def print_info(self):
        super().print_info()    # call the print_info() method of Vehicle class
        print(self.no_of_tyres, self.no_of_seats)

# Another child class which inherits from Vehicle class
class Bike(Vehicle):
    def __init__(self, make, model, year, top_speed):
        Vehicle.__init__(self, make, model, year)
        self.speed = top_speed

    def print_info(self):
        super().print_info()
        print(self.speed)

swift = Car('Maruthi Suzuki', 'Swift', '2017', 5)
swift.print_info()

pulsar = Bike('Honda', 'Pulsar', '2015', 200)
pulsar.print_info()