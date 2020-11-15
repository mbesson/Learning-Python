# Playing around with the for loop

colors = ['blue', 'green', 'purple']

for color in colors: # for variable in collection/something that yiels a result
    print(color)

for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)

point = (2.1,3.0,7)
for value in point:
    print(value)

ages = {'Kevin':24, 'MAthieu': 29}

for key in ages:
    print(f"{key} is {ages[key]}") # Don't modifi anything inside a loop

for letter in "Mathieu":
    print(letter)

list_of_points = [(1,2),(3,4)]

for x,y in list_of_points:
    print(f"x: {x}, y: {y}")

    


