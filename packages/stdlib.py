# Working with the standard library

# How can we use the standard livrery in oor code?

# Python modul index is an idex about what's in the std libray

import math # This is the synt  xe to import to whole module
math.pi
math.ceil

# but we can dio better
from math import pi,ceil # With this you know exactly what's going on
pi # we can access to pi

from math import pi as p 
from math import * # iport everuthing that is expose in the library into the namespace
# The problem is that you don't know what is what

# math modul
# argparse : for command line interface for example
# json
# os module
# sys module
# pdb : pytnon debugger