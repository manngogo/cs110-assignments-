import math
import stdio
import sys
#import in order to use
#import variables as different names pre conversion
a = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])
#converting variables from degrees to radians
θ1 = math.radians(a)
#manipulated given equation
sinθ2 = (n1 * math.sin(θ1))/n2
#take the inverse of sine to get the value of just theta 2 in radians
#got the asin from acos from previous problems. acos is inverse of cos, so...
θ2r = math.asin(sinθ2)
#convert the radians into degrees
θ2d = math.degrees(θ2r)
#print out the theta 2 value
stdio.writeln(θ2d)