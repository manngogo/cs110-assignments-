import math
import stdio
import sys
#imported to use
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
#If a is equal to zero then the equation is not quadratic
if a == 0:
    stdio.writeln('Value of a must not be 0')
    sys.exit(1)
#Discriminant equation because its easier to do the if statement with it
discriminant = b**2 - 4*a*c
#Discriminant must be greater than or equal to zero to find the square root
if discriminant < 0:
    stdio.writeln('Value of discriminant must not be negative')
    sys.exit(1)
else:
    answer1 = (-b + math.sqrt(discriminant)) / (2*a)
    answer2 = (-b - math.sqrt(discriminant)) / (2*a)
    stdio.write(f' {answer1} {answer2}')
#Answer to appear like it does in the pdf
