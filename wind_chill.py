import stdio
import sys
#imported to use
#variables as given
t = float(sys.argv[1])
v = float(sys.argv[2]) #accepts argument 2 as a float named v
#if statements as directed in the pdf
if t > 50:
    stdio.writeln('Value of t must be <= 50 F')
    sys.exit(1)
elif v <= 3:
    stdio.writeln('Value of v must be > 3 mph')
    sys.exit(1)
else:
    w = 35.74 + (0.6215 * t) + (((0.4275 * t) - 35.75) * (v ** 0.16)) #equation provided in the pdf
#print out w
stdio.writeln(w)