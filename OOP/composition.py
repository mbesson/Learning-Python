# Understanding composition
# Confused for other thing
# building classes by passing other instance of classes

class Tire:
    """
    Tire represent a tire in an automobile
    """
    def __init__(self, tire_type, width):
        self.tire_type = tire_type
        self.width = width
    def __repr__(self): # The representation of the Tire
        """
        Represents the tire in stndart notation
        """
        return (f"{self.tire_type}/{self.width}")
    def circumference(self):
        """
        The circumference of the tire in inches
        python3.7 -m doctest -v tire.py
        >>> tire = Tire('A',3)
        >>> tire.circumference()
        >>> 6
        """
        side_wall = 2
        total_diameter = 3*2
        return total_diameter

# ptyhon3.7 -i myFile.py
#from tire import Tire
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
    def wheel_circumference(self):
        return self.tires[0].circumference()

    
tire = Tire('A','B')
tires = [tire,tire,tire,tire]

q2 = Car(tires=tires,engine='4-cylinders')
q2.description()
q2.wheel_circumference()

