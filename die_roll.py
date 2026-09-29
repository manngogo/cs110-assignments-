import stdio
import stdrandom
import sys
#import to make use of
#variables as given
n = int(sys.argv[1])
#rolling n sided dice twice, from 1 because a dice has at least 1 on its value
n1 = stdrandom.uniformInt(1, n + 1)
n2 = stdrandom.uniformInt(1, n + 1)
#print out the sum of the 2 dice rolls
stdio.writeln(n1 + n2)
#Changed to n+1 because autograder failed it and when I tried to see, I wasn't able to actually get a value of n
