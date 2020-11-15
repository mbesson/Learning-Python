# Understand Conditionals and comparison
1 <2
1 >2
1>=2
1<=2
1 == 2
1==1
1==1.0 # because they are ewuivalent

'a' == 'a'
'a' == 'A'

3.1 == 'this' # still ok
3.1 >= 'this' # gives errors

'b' >'a'

1!=2

# This is the 2 basics type of comparison

'abc' < 'b' 
'bac' <'b'

# in key word
2 in [1,2,3]
4 in [1,2,3]

2 not in [1,2,3]
4 not in [1,2,3] # You can go form sudo code to real code

# Now conditionak
# IF
# ELIF
# ELSE

if True:
    print('Was TRUE')# Python works with indentation

if 1>2:
    print('was true')
else:
    print('was false')


name = 'Mathieu'
name
if len(name) >=3:
    print('Name is long')
elif len(name)==7:
    print("Exactly 7 nice!!")
else:
    print("noting to say")


