import stdio
import sys
#import to use

# n = index of the last row of the triangle (so there are n + 1 rows).
n = int(sys.argv[1])
 
# triangle[i] will hold row i of Pascal's triangle, which has i + 1 entries.
triangle = []
 
for i in range(n + 1):
    # Start row i as all 1s. This handles the rule P(i, 0) = P(i, i) = 1
    # for free, since the first and last entries are never changed below.
    row = [1] * (i + 1)
 
    # Fill in the interior entries (columns 1 .. i-1). For rows 0 and 1 the
    # range is empty, so the loop correctly does nothing.
    for j in range(1, i):
        # Each interior entry is the sum of the two entries above it
        # in the previous row: P(i-1, j-1) + P(i-1, j).
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
 
    # Save the finished row so the next row can use it.
    triangle.append(row)
 
# Write the triangle, one row per line, entries separated by spaces.
for i in range(n + 1):
    for j in range(i + 1):
        if j < i:
            stdio.write(f'{triangle[i][j]} ')
        else:
            stdio.write(f'{triangle[i][j]}\n')