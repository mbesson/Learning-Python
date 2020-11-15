# And now, let's get our hands dirty withl list

# A list is an ordere sequence of items
list('abc') # gives 'a', 'b', 'c']

my_list = [1,2,3,4,5]
my_list

my_list[4]

my_list[7] # index out of ranges

len(my_list) # Index starts at 0
my_list[len(my_list) - 1]

#Slicing feature
my_list[0:2] # Start at 0 and give me everything before de 2 exlusion
my_list[1:3]
my_list[:2]
my_list[::2] # start:end:step
# The step can be negative : usefull to revers a list
my_list[::-1]

# List modification
my_list[0] = "a"
my_list # lists ar mutable

my_list[0:2] = 'b'
my_list

my_list = [1,2,3,4,5]
my_list[0:2] = [] # You can delete a section of a list here
my_list

# Common methods
## Remove
my_list.remove(6) # x not in the list
my_list.remove(4)
my_list

## pop
my_list.pop() # You can use it as a stack LIFO

# If you want to use a queue use a pop(0) FIFO

## Append
my_list.append(6)
my_list

my_list.insert(1,3) # insert(index,item)
my_list

