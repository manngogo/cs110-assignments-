import stdio
import sys
#imported to use their commands
# accepting as commands according to instructions in the pdf
m = int(sys.argv[1]) 
d = int(sys.argv[2]) 
y = int(sys.argv[3]) 
#inputting the provided equations
#equations were wrong but someone in the discord left a response
#mod = modulo, got me confused for a bit but the idea of a remainder
y0 = y - ((14-m)//12)
x0 = y0 + (y0//4) - (y0//100) + (y0//400)
m0 = m + 12 * ((14-m)//12) - 2
dow = ((d + x0 + (31 * m0) //12)) % 7
#print out the result
stdio.writeln(dow)
