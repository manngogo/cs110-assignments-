import stdrandom
import stdio
#import to use
# Number of measures in each part of the waltz.
MEASURES = 16
 
# mozart.txt contains only the two tables (no header lines): first the
# minuet table (11 rows x 16 columns), then the trio table (6 rows x 16 columns).
# stdin is a stream of ints, so we read them all at once and then walk through
# the list with an index.
data = stdio.readAllInts()
pos = 0   # index of the next unread number in data
 
# read the minuet table
minuet_rows = 11              # one row per dice sum 2..12
minuet_cols = 16              # one column per measure
 
minuet = []
for i in range(minuet_rows):
    row = []
    for j in range(minuet_cols):
        row.append(data[pos])
        pos += 1
    minuet.append(row)
 
# ---- Read the trio table ----
trio_rows = 6                 # one row per die roll 1..6
trio_cols = 16                # one column per measure
 
trio = []
for i in range(trio_rows):
    row = []
    for j in range(trio_cols):
        row.append(data[pos])
        pos += 1
    trio.append(row)
 
# generate the waltz
waltz = []
 
# Minuet: for each of the 16 measures, roll two dice and sum them.
for measure in range(MEASURES):
    roll = stdrandom.uniformInt(1, 7) + stdrandom.uniformInt(1, 7)   # between 2 and 12
    # The table's first row is for a roll of 2, so row index = roll - 2.
    waltz.append(minuet[roll - 2][measure])
 
# Trio: for each of the 16 measures, roll ONE die.
for measure in range(MEASURES):
    roll = stdrandom.uniformInt(1, 7)   # between 1 and 6
    # The table's first row is for a roll of 1, so row index = roll - 1.
    waltz.append(trio[roll - 1][measure])
 
# Write all 32 measure numbers on one line, separated by spaces.
# The minuet numbers (1..176) and trio numbers (1..96) are written as-is;
# playwaltz.py knows that the first 16 are minuet and the last 16 are trio.
for i in range(len(waltz)):
    if i < len(waltz) - 1:
        stdio.write(f'{waltz[i]} ')
    else:
        stdio.write(f'{waltz[i]}\n')