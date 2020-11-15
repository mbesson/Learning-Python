# Fun with dictionnaries

# hashes or associative arrays

ages = {'Mathieu': 29, 'alex': 40, 'bob': 35}
ages

ages['Mathieu']

#Keys can be immutable data types

{[1,2,3]: True} # this hives an erros
# Dictorionnaries works pretty much like a data base

ages['Robert'] # gives a keyError

ages['Robert'] = 32
ages

ages['Robert'] = 33
ages

# Removing
del ages['Robert'] # del works also to remove variable
ages

ages['Robert'] = 33
ages
ages.pop('Robert') # pop is safer for removing
ages

# Safer way to read
ages.get('MAthieu')

list(ages.keys())

ages.values() # gives a dict but you can pass it in a list

weights = dict(kevin=30,Mathieu=29,bob=40)
weights

colors = dict([('Kev', 'blue'),('Mat','red')]) # list of tuples
colors