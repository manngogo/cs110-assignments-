import math
import stdio
import sys
#import to use these variables
#variables per instructions
λ = float(sys.argv[1]) #just copied it from the pdf idk if this is right
t = float(sys.argv[2])
#equation per instruction
p = math.exp(-λ * t) #math function in order to use e
#writes probability p to standard output
stdio.writeln(p)
