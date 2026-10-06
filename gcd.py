import stdio
import sys
#imported to use
#variables as in pdf
p = int(sys.argv[1])
q = int(sys.argv[2])
#Euclidean algorithm to find gcd
while q != 0:
    r = p % q
    p = q
    q = r
#final result
stdio.writeln(p)