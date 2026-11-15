import stdaudio
import stdio
import sys
#import to use
MEASURES = 16        # measures in the minuet, and also in the trio
MAX_MINUET = 176     # minuet measures are M1.wav .. M176.wav
MAX_TRIO = 96        # trio measures are T1.wav .. T96.wav
 
# read all 32 (we hope) integers from standard input.
waltz = stdio.readAllInts()
 
#need to validate before playing audio, if error, no audio may play
# order of the checks matters: we must check the length first, bc the later gives error 
# Check 1: a waltz is exactly 32 measures.
if len(waltz) != 2 * MEASURES:
    sys.exit('A waltz must contain exactly 32 measures')
 
# Check 2: the first 16 numbers are minuet measures, each in [1, 176].
for i in range(MEASURES):
    if waltz[i] < 1 or waltz[i] > MAX_MINUET:
        sys.exit('A minuet measure must be from [1, 176]')
 
# Check 3: the last 16 numbers are trio measures, each in [1, 96].
for i in range(MEASURES, 2 * MEASURES):
    if waltz[i] < 1 or waltz[i] > MAX_TRIO:
        sys.exit('A trio measure must be from [1, 96]')
 
# if all inputs are valid, can play
 
# Play the minuet (first 16 measures) from files 
for i in range(MEASURES):
    stdaudio.playFile(f'data/M{waltz[i]}')
 
# Play the trio (last 16 measures) from files
for i in range(MEASURES, 2 * MEASURES):
    stdaudio.playFile(f'data/T{waltz[i]}')
