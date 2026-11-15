import stdio
import sys
#imported all to use for the code
# m = number of rows, n = number of columns of the INPUT matrix.
m = int(sys.argv[1])
n = int(sys.argv[2])
 
# Read the m by n matrix into a 2D list: a list of m rows, each row a list
# of n floats. a[i][j] is the element in row i, column j.
a = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(stdio.readFloat())
    a.append(row)
 
# The transpose b is n x m, with b[i][j] = a[j][i].
# Instead of building b explicitly, we can just print it directly:
# the outer loop goes over the rows of b (i from 0 to n-1, which are the
# columns of a) and the inner loop goes over the columns of b (j from 0 to m-1,
# which are the rows of a).
for i in range(n):
    for j in range(m):
        if j < m - 1:
            stdio.write(f'{a[j][i]} ')   # a[j][i], NOT a[i][j]: that's the transpose
        else:
            stdio.write(f'{a[j][i]}\n')  # newline after the last entry in the row
 