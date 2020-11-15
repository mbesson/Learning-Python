# Logic Operations

#or
#and
#not

bool("")
not ""

not 1 > 2 # Gives True because the precedence is 1 > 2 giv False ans not False gives True

if not 1 > 2:
    print("Not it isn't")

'' or 'Math'
'' or 0
'Math' or 0 # gives the first truthy value

first = ""
last = 'Mathieu'

if first or last:
    print("User has a part of a name")

if first and last:
    print("User has a full name")

