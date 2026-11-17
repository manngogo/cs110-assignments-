import math
import stdio
import sys

# this program reads a number n from the command line, then reads two vectors of n floats each from 
# standard input (first all of x, then all of y), and writes the Euclidean distance between them. 
# main() below does the reading and writing, and calls our _distance() function to do the math.
# Entry point (DO NOT EDIT).
def main():
    n = int(sys.argv[1])
    x, y = [], []
    for i in range(n):
        x += [stdio.readFloat()]
    for i in range(n):
        y += [stdio.readFloat()]
    stdio.writeln(_distance(x, y))


# Returns the Euclidean distance between the vectors x and y.
def _distance(x, y):
    # The Euclidean distance is sqrt( (x0 - y0)^2 + (x1 - y1)^2 + ... ).
    # Step 1: keep a running total of the squared differences, starting at zero.
    total = 0.0

    # Step 2: visit every position of the vectors (they have the same length, so we can
    # use the length of x for both).
    for i in range(len(x)):
        # Find the difference between the two entries at this position.
        diff = x[i] - y[i]
        # Square the difference and add it to the total. We compute diff first and then
        # multiply it by itself; writing x[i] - y[i] ** 2 would be wrong because ** is
        # done before subtraction, so only y[i] would be squared.
        total += diff * diff

    # Step 3: take the square root ONCE, after every squared difference has been added.
    # (Taking a square root inside the loop would be wrong, because the square root of a sum is not the sum of the square roots.)
    return math.sqrt(total)


if __name__ == "__main__":
    main()