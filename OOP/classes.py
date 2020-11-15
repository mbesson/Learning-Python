# Dive into OOP
# What is an object? functionality with methods
# Modeling concepts of our world

class Car: # traditionnaly starts with capital letter and camel case
    """
    Car models a car w/ tires and engine
    """
    def __init__(self, engine, tires): # This will create an instance of a class
        """
        Dcstring describing the method
        dunder method (Double under)
        """
        #pass # we do not implement right now
        self.engine = engine
        self.tires = tires
    # MEthod and function are the same things but method are attached to an object
    # There is always a self even if it it not used whan calling the method
    def description(self):
        print(f"A car with {self.engine} and {self.tires}")

my_car = Car('4-cylinder',['front-driver','front-passenger'])
my_car # This is an instance of the class Car
my_car.engine
my_car.tires

my_car.licence_plate = 'someting'
my_car.licence_plate # yes you can do it even if you will not see it very often

my_car.description()

