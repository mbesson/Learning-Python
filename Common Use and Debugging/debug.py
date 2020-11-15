# Debugger
# Stop our code as it is executed
# Insepct data end so one

#import pdb
def map(func, values):
    output_values = []
    index = 0
    while index < len(values):
        output_values.append(func(values[index]))
        index +=1
    return output_values

def add_one(val):
    return val+1

print(map(add_one, list(range(10))))

# Alternatively, we can do python -m pdb debug.py

# We can set breakpoint. For example, we can use break 10, index == 5 (the last part is the condition)