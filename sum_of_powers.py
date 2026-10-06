import stdio
import sys
#imported to use
#variables as in pdf
n = int(sys.argv[1])
k = int(sys.argv[2])
#equation for the 1^k + 2^k + 3^k + ... + n^k
sum = 0
for i in range(1, n + 1):
    sum += i ** k
#final result
stdio.writeln(sum)