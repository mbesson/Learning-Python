# Encapslutating code in pyhton

# Create code ines and re-use it

def hello_world():
    print("Hello, world!")

hello_world() # First class citizen -> pass as variables to call them so to use the fucntion myste us parenthesis

def print_name(name):
    print(f"Name is {name}")

print_name("Mathieu")

output = print_name("Robert") # By default, function don't return anything to use

def add_two(num):
    return num + 2 # We must use keyword return

result = add_two(2)
result

def add(num1, num2):
    return num1 + num2

add(1,5)

def contact_card(name, age, car_model):
    print(f"{name} is {age} and drives a {car_model}")

# With positionnal arguments
contact_card('Mathie', 29, "Q2")

# With keyword arguments
contact_card(age=29, car_model="Q2", name = "Mathieu")
#Positional argument first is we want to mixe types of arguments

# Default arguments

def can_drive(age, driving_age = 16):
    return age >= driving_age

can_drive(15)
can_drive(15,14)
