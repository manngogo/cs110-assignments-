import stdio
import sys
#imported to use
#variables as given
t = float(sys.argv[1]) #accepts argument 1 as a float named 5
v = float(sys.argv[2]) #accepts argument 2 as a float named v
w = 35.74 + (0.6215 * t) + (((0.4275 * t) - 35.75) * (v ** 0.16)) #equation provided in the pdf
#print out w
stdio.writeln(w)