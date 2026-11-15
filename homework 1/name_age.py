import stdio
import sys
#imported to use for program
name = sys.argv[1] #To make it easier to concatenate, I defined the variable
age = sys.argv[2] #Same as above line
stdio.write(f' {name} is {age} years old.') #Concatenated the text so it would take less lines of code to produce a working output, seems to work
#Was originally unsure if this format would work but it seems to work well when tested, so leaving it like this.