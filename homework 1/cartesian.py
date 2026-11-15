import math
import stdio
import sys
#imported to use
#defining variables given
r = float(sys.argv[1])
degrees = float(sys.argv[2])
#converting degrees to radians because thats what is expected in math.cos/sin
θ = math.radians(degrees)
#convert the given coordinates into cartesian form with these equations for x and y
x = r * math.cos(θ) #had to look up how to use math library for cosine function
y = r * math.sin(θ) #didn't need to look it up, just tried to see if it worked because thats how the cosine function was written
#writes values to standard output seperated by a space
stdio.writeln(f'{x} {y}') #originally did like ({x}, {y}) but it said writeln() takes from 0-1 positional arguments but 2 were given, so i did the f'' again