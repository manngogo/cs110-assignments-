import math
import stdio
import sys
#import to use
# Command-line arguments are always strings, so convert n to an int.
n = int(sys.argv[1])
 
# Read the first vector: n floats from standard input.
# We read them one at a time with readFloat() because we know exactly
# how many to expect.
x = []
for i in range(n):
    x.append(stdio.readFloat())
 
# Read the second vector the same way. Because stdin is just a stream of
# tokens, the first n floats go to x and the next n floats go to y, regardless of line breaks.
y = []
for i in range(n):
    y.append(stdio.readFloat())
 
# Euclidean distance = sqrt( sum of (x[i] - y[i])^2 ).
# We accumulate the sum of squared differences in a running total.
total = 0.0
for i in range(n):
    diff = x[i] - y[i]
    total += diff * diff   # diff * diff avoids any floating-point issues which i previously had
# Take the square root only once, at the end, after summing everything.
stdio.writeln(math.sqrt(total))
 