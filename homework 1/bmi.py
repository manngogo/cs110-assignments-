import stdio
import sys
#import to use
weight = float(sys.argv[1]) #variable as float
height = float(sys.argv[2]) #variable as float
bmi = weight / (height ** 2) #bmi equation
stdio.writeln(bmi) #print out bmi value