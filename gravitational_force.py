import stdio
import sys
# imported to use
#variables as floats as per instructions
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])
G = 6.674 * (10**-11) #put this equation first bc it is used as a variable in f, and you need G to be defined first
f = G * ((m1 * m2)/(r**2)) #equation given
stdio.writeln(f) #print the f value