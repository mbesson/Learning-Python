# Tuples and ranges

# They are immutables!

# First tuple : fixew width immutable sequence type

point = (2.0,3.0) # Use the parenthese and separete with a comma
point
point[0] = 1 # GIves and error

point_3d  =point + (4.0,) # need to put the comma to specified we don't put other things
point_3d

# We can unpack then into variable
x,y,z=point_3d
x
y
z

print("My name is : %s %s"%("Mathieu","Besson"))

# You can't change the mength and items in tuples

#Second ranges

range(10) # 0 is the start and stop

list(range(10))

range(0,10000) # it is faster than doing a list

#step value
list(range(1,12,2))