import math
import stdio
import sys
#import to make use of
#variables as per instructions
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
d = float(sys.argv[4])
#converting degrees to radians for the math library to work
x1 = math.radians(a)
y1 = math.radians(b)
x2 = math.radians(c)
y2 = math.radians(d)
#had to look up how to do arccos on math library
#inputted function as given
d = 6359.83 * math.acos((math.sin(x1)*math.sin(x2))+(math.cos(x1) * math.cos(x2) *math.cos(y1-y2)))
#print out the result
stdio.writeln(d)