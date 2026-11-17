import stdarray
import stdio
import sys


# program reads the number of rows m and columns n from the command line, reads an m-by-n matrix of floats from standard input, 
# and writes its transpose.
# main() below creates the matrix a, fills it, calls our _transpose() function, and writes each row of the result on its own line.
# Entry point (DO NOT EDIT).
def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    a = stdarray.create2D(m, n)
    for i in range(m):
        for j in range(n):
            a[i][j] = stdio.readFloat()
    c = _transpose(a)
    for row in c:
        for v in row:
            stdio.write(str(v) + " ")
        stdio.writeln()

# Returns the transpose of a.
def _transpose(a):
    # Step 1: work out the shape of a. m is the number of rows (how many lists are inside a), and 
    # n is the number of columns (the length of the first row).
    m = len(a)
    n = len(a[0])

    # Step 2: create a brand new matrix to hold the answer. The transpose of an m-by-n matrix is n-by-m, so it has n rows and m columns. 
    # (Using create2D(m, n) here would only work for square matrices.) Result is n-by-m, with c[i][j] = a[j][i].
    c = stdarray.create2D(n, m)

    # Step 3: fill in the new matrix. i walks over the n rows of the result and j walks over its m columns.
    for i in range(n):
        for j in range(m):
            # Row i, column j of the result is row j, column i of the original: the rows and columns swap places.
            c[i][j] = a[j][i]

    # Step 4: give the new matrix back to the caller. The original matrix a is unchanged.
    return c


if __name__ == "__main__":
    main()
