import stdio
import sys
#imported to use
#variable in pdf
n = int(sys.argv[1])
#find perfect numbers
for i in range(2, n + 1):
    divisors = []
    for j in range(1, i):
        if i % j == 0:
            divisors.append(j)
    if sum(divisors) == i:
        stdio.writeln(i)
#print result
