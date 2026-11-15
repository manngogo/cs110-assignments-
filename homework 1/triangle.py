import stdio
import sys
#import to use 
#variables as given
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
#less than or equal to the sum of the other 2
a = (x<=(y+z)) and (y<=(x+z)) and (z<=(y+x))
#print as true or false 
stdio.writeln(a)