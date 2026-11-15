import stdio
import sys
#import to be able to use the functions
#variables according to instructions
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])
#input the equations given
q = 1 - p
p1 = (1-((p/q)**n2))/(1-((p/q)**(n1+n2)))
p2 = (1-((q/p)**n1))/(1-((q/p)**(n1+n2)))
#print the results so you can see it when you run the program 
stdio.writeln(f' {p1} {p2}')