# Start classes with Uppercase naming like Animal, Person

class Dog:

    # will store in each instances
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # function of choice
    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


# accessing attributes
my_dog = Dog("Larry", 1)
your_dog = Dog('Barry', 3)


# print(my_dog.name, my_dog.age)
# calling class methods after creating object
# my_dog.sit()
# your_dog.sit()
# my_dog.roll_over()


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # default value for an attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        print(f"This {self.year} {self.make} {self.model} has {self.odometer_reading} kilometers on it.")

    def update_odometer(self, kilometers):
        if kilometers >= self.odometer_reading:
            self.odometer_reading = kilometers
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers


my_car = Car("Nissan", "Silvia S14", 1998)
my_car.update_odometer(65000)
print(my_car.get_descriptive_name())
my_car.read_odometer()

my_car.update_odometer(75000)
my_car.read_odometer()

my_car.increment_odometer(130)
my_car.read_odometer()


# Can add instances as Attributes
class Battery:
    def __init__(self, battery_size=100, distance_range=31):
        self.battery_size = battery_size
        self.distance_range = distance_range

    def describe_battery(self):
        print(f"This car has a {self.battery_size}--kWh battery.")

    def get_range(self):
        if self.battery_size <= 75:
            self.distance_range = 260
        elif self.battery_size <= 100:
            self.distance_range = 315
        else:
            self.distance_range = 'Unknown'

        print(f"This car can go about {self.distance_range} miles on a full charge.")


# Child classes ( Inheritance )
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # use super to use the initial attributes of the parent class
        super().__init__(make, model, year)
        # can add more attributes for child class
        self.battery = Battery()


my_electric_car = ElectricCar('Tesla', 'model s', 2019)
my_electric_car.battery.battery_size = 120
# Can use methods from parent class
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()

# Can import single, multiple and even the whole module of classes similar to importing functions
# Can use aliases for module or certain classes similar to functions
