import rsa
import stdio
import sys


# Overview: this program encrypts a message. It reads the public key n and e from the command
# line and the message from standard input, and writes each character of the message,
# encrypted, as a binary number of the same width.
# Entry point.
def main():
    # Step 1: read the public key. These arrive as strings, so convert them to ints.
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # Step 2: read the entire message from standard input as one string. readAll() keeps
    # every character, including spaces and the final newline if you pressed Enter before
    # Ctrl-D, so the newline is encrypted too.
    message = stdio.readAll()

    # Step 3: decide how wide each encrypted character will be. An encrypted value is
    # always smaller than n, so bitLength(n) bits are enough for every one. Using the same
    # width for every character is what lets decrypt.py split the stream of bits again,
    # even though there are no spaces between the characters.
    # Each encrypted character is written as a binary number of fixed width.
    width = rsa.bitLength(n)

    # Step 4: go through the message one character at a time.
    for c in message:
        # ord(c) turns the character into its number (for example 'C' becomes 67), because
        # RSA encrypts numbers, not letters. n must be bigger than 127 so every ASCII
        # character fits.
        y = rsa.encrypt(ord(c), n, e)

        # Write the encrypted number in binary, padded with leading zeros to the fixed
        # width. We use write (not writeln) so all the bits end up on one line.
        stdio.write(rsa.dec2bin(y, width))

    # Step 5: finish the line of bits with a newline.
    stdio.writeln()


if __name__ == "__main__":
    main()