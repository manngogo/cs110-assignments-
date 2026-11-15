import stdio
import sys
#imported to use
#variables in pdf
n = int(sys.argv[1])
#equation given
a = 1
while a ** 3 + (a + 1) ** 3 <= n:
    b = a + 1
    while a ** 3 + b ** 3 <= n:
        c = a + 1
        while c ** 3 + (c + 1) ** 3 <= n:
            d = c + 1
            while c ** 3 + d ** 3 <= n:
                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                    stdio.writeln(f'{a ** 3 + b ** 3} = {a}^3 + {b}^3 = {c}^3 + {d}^3')
                d += 1
            c += 1
        b += 1
    a += 1