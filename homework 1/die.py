import stdio
import stdrandom
#imported to use
#die roll equation, had to do 7 because the upper bound is exclusive
d = stdrandom.uniformInt(1, 7)
#if elif statements, had to do writeln for the multiple lines of output and it would come out neatly
if d == 1:
    stdio.writeln('*')
elif d == 2:
    stdio.writeln('*    \n     \n    *')
elif d == 3:
    stdio.writeln('*    \n  *  \n    *')
elif d == 4:
    stdio.writeln('*   *\n     \n*   *')
elif d == 5:
    stdio.writeln('*   *\n  *  \n*   *')
else:
    stdio.writeln('* * *\n     \n* * *')
