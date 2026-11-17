import rsa
import stdio
import sys


# Overview: this program generates an RSA key. It reads lo and hi from the command line (the
# interval [lo, hi) the two primes are picked from) and writes the keys n, e and d on one
# line, separated by spaces. The public key is (n, e) and the private key is (n, d).
# Entry point.
def main():
    # Step 1: read the two interval ends. Command-line arguments are always strings, so
    # each one must be converted to an int before it can be used as a number.
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # Step 2: let the rsa library do the work. It returns a tuple (n, e, d), which we
    # unpack into three separate variables.
    n, e, d = rsa.keygen(lo, hi)

    # Step 3: write the three numbers separated by spaces, followed by a newline.
    # %d means "put an integer here".
    stdio.writef("%d %d %d\n", n, e, d)


if __name__ == "__main__":
    main()
