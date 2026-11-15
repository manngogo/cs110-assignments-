import stdio
import stdrandom
#imported to use
#card roll equation, had to do 14 because the upper bound is exclusive
c = stdrandom.uniformInt(1, 14)
#rank selection because when I did stdio.writeln it would print it above the output
if c == 1:
    rank = 'Ace'
elif c == 2:
    rank = '2'
elif c == 3:
    rank = '3'
elif c == 4:
    rank = '4'
elif c == 5:
    rank = '5'
elif c == 6:
    rank = '6'
elif c == 7:
    rank = '7'
elif c == 8:
    rank = '8'
elif c == 9:
    rank = '9'
elif c == 10:
    rank = '10'
elif c == 11:
    rank = 'Jack'
elif c == 12:
    rank = 'Queen'
elif c == 13:
    rank = 'King'
#random suite generator
suite = stdrandom.choice(['Hearts', 'Diamonds', 'Clubs', 'Spades'])
#final result concatenated statement
stdio.writeln(rank + ' of ' + suite)