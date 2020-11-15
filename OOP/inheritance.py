# Having fun with inheritance

# Do not mess it with comosition

# You can create a class based on a difference class
# Ex : a "shape" class

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

# Creating a sub class
class SnowTire(Tire): # multiple class passing is possible but it is a bad idea
    def __init__(self, tire_type, width, chain_thickness):
        Tire.__init__(self, tire_type, width)
        self.chain_thickness = chain_thickness
    
    def circumference(self):
        """
        The circumference of a snow tire
        We could add some more tests...
        """
    
    def __repr__(self):
        return super() + " (Snow)"














