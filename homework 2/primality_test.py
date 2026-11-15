import stdio
import sys
#imported to use
#variable in pdf
n = int(sys.argv[1])
# Numbers below 2 are not prime
is_prime = n >= 2
# Look for a divisor up to sqrt(n)
i = 2
while is_prime and i * i <= n:
    if n % i == 0:
        is_prime = False
    i += 1

stdio.writeln(is_prime)