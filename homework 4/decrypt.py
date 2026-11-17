import rsa
import stdio
import sys


# program decrypts a message made by encrypt.py. It reads the private key n and
# d from the command line and the message (a long string of 0s and 1s) from standard input,
# and writes the original text.
# Entry point.
def main():
    # Step 1: read the private key which arrive as strings, so convert them to ints.
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    # Step 2: read all the bits. readAllStrings() splits the input at whitespace and returns a LIST of strings (for example when the input ends with a newline, or is spread over
    # several lines), so we join the pieces together with "" to get one long bit string. Join the whitespace-separated tokens to get the full bit string.
    bits = "".join(stdio.readAllStrings())

    # Step 3: work out how many bits belong to each character. This must be the same width that encrypt.py used, which depends only on n.
    width = rsa.bitLength(n)

    # Step 4: cut the bit string into pieces of width bits. range(0, len(bits), width) makes i jump forward by width each time (0, width, 2 * width, ...), so the pieces dont overlap.
    for i in range(0, len(bits), width):
        # Take the next piece and convert it from binary to an ordinary integer.
        y = rsa.bin2dec(bits[i:i + width])
        # Decrypt that integer with the private key to get the character's number back,
        # turn the number into a character with chr(), and write it. We use write (not
        # writeln) so the characters appear next to each other, like the original text.
        stdio.write(chr(rsa.decrypt(y, n, d)))


if __name__ == "__main__":
    main()