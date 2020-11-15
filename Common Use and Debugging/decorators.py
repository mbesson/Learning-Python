# Understanding decorators
# pass around function (comming for functional programming)

# Writung Higer Ordr Functions

# First HOF
def inspect(func): # * alow use to pack or unpack. ** do the same thing with keywrod arguments. Alow to create a variatic function
    def wrapped_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        val = func(*args, **kwargs)
        print(f"Result: {val}")
    return wrapped_func

@inspect
def combine(a, b):
    return a+b

# python -i decorators.py
# inspect(combine, 1, 2)
# inspect(combine, 1, 2, 3) will fail 

# calssmethod, static method and property decorators

class User:
    base_url = 'https://example.com/api'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def query(cls, query_string): # We will have access to User.query()
        return cls.base_url + '?' + query_string

    @staticmethod # It doesn't require additional arguments.It can take arguments though, lke query_string in our class method though
    def name(): # Bind to namespace User
        return 'Kevin Bacon'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    
    



