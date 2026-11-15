import stdio
import sys
#imported to use
n = int(sys.argv[1])
#outputs the nth fibonacci number
a = 0   # F(0)
b = 1   # F(1)
for _ in range(n):
    temp = a + b
    a = b
    b = temp
#prints the output
#this will go on until n passes through the loop
stdio.writeln(a)