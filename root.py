import stdio
import sys
#imported to use
#variables as per pdf
k = int(sys.argv[1])
c = float(sys.argv[2])
epsilon = float(sys.argv[3])
# Initial guess
x = c
# Newton's method: x = x - (x^k - c) / (k * x^(k-1))
# Keep going until x is within a relative tolerance of c / x^(k-1),
# which equals x once x is the true k-th root
while abs(x - c / x ** (k - 1)) > epsilon * x:
    x = x - (x ** k - c) / (k * x ** (k - 1))

stdio.writeln(x)