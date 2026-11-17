import stdio
import stdrandom
import sys


# this library implements the RSA public-key cryptosystem.
#   - A key has three numbers: n and e (the PUBLIC key, which anyone may know) and
#     d (the PRIVATE key, which only the receiver knows).
#   - To encrypt a number x we compute  x^e mod n.
#   - To decrypt an encrypted number y we compute  y^d mod n, which gives x back.
# helper functions at the bottom (_primes, _sample, _choice) support keygen().
# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).

def keygen(lo, hi):
    # Step 1: pick two DIFFERENT random primes p and q from [lo, hi). _sample picks without
    # replacement, so p and q can never be the same number.
    p, q = _sample(_primes(lo, hi), 2)

    # Step 2: n is the product of the primes. It is part of both the public and private key.
    n = p * q

    # Step 3: m = (p - 1)(q - 1). It is only used while building the keys (e and d), and is never published.
    m = (p - 1) * (q - 1)

    # Step 4: pick a random prime e < m such that e does not divide m. Instead of listing every prime below m (slow for large m), keep 
    # drawing random numbers from [2, m) until one is prime (_primes(e, e + 1) is non-empty only when e is prime) and doesnt divide m
    e = stdrandom.uniformInt(2, m)
    while len(_primes(e, e + 1)) == 0 or m % e == 0:
        e = stdrandom.uniformInt(2, m)

    # Step 5: e * d mod m == 1. We find it by trying d = 1, 2, 3, ... until equation holds. always exists b/c e is a prime that doesnt divide m.
    d = 1
    while (e * d) % m != 1:
        d += 1

    # Step 6: return all 3 #s as a tuple.
    return n, e, d


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    # pow(x, e, n) computes (x ** e) % n using modular exponentiation. It reduces mod n
    # as it goes, so it never builds the gigantic number x ** e. x must be less than n.
    return pow(x, e, n)


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    # Same idea as encrypt, but with the private exponent d. This undoes encrypt().
    return pow(y, d, n)


# Returns the least number of bits needed to represent n.
def bitLength(n):
    # bin(n) gives a string like '0b1010011'. The first two characters are the '0b'
    # prefix, so the number of binary digits is the length minus 2.
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, padded w/ leading zeros.
def dec2bin(n, width):
    # The format "0<width>b" means: binary, padded on the left with zeros to <width> digits.
    # "0%db" % (width) builds that format string, for example "07b" when width is 7.
    return format(n, "0%db" % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    # int(string, 2) reads the string as a base-2 number and returns the ordinary integer.
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    # Collect the primes we find in this list.
    primes = []

    # Check every number in the interval. Primes start at 2, so skip anything below 2
    for n in range(max(lo, 2), hi):
        # n is prime if no number from 2 up to sqrt(n) divides it evenly.
        # We only need to go up to sqrt(n) because any factor larger than that would be paired with a factor smaller than that.
        isPrime = True
        i = 2
        while i * i <= n:
            if n % i == 0:
                # Found a divisor, so n is not prime. No need to look further.
                isPrime = False
                break
            i += 1
        # If no divisor was found, remember n.
        if isPrime:
            primes += [n]
    return primes


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    # Partial Fisher-Yates shuffle on a copy of a; the first k items form the sample. Work on a copy (a[:]) so the caller's list isnt rearranged.
    b = a[:]
    n = len(b)

    # For each of the first k positions, choose a random item from the not-yet-chosen part of the list (positions i up to n - 1) and swap it into position i.
    for i in range(k):
        j = stdrandom.uniformInt(i, n)
        b[i], b[j] = b[j], b[i]

    # The first k positions now hold k different randomly chosen items.
    return b[:k]


# Returns a random item from the list a.
def _choice(a):
    # Pick a random position from 0 to len(a) - 1 (the upper bound of uniformInt is
    # exclusive) and return the item stored there. keygen no longer needs this helper, but kept as a general-purpose utility.
    return a[stdrandom.uniformInt(0, len(a))]


# Unit tests the library [DO NOT EDIT].
def _main():
    c = sys.argv[1]
    x = ord(c)
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef("encrypt(%c) = %d\n", c, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef("decrypt(%d) = %c\n", encrypted, chr(decrypted))
    width = bitLength(x)
    stdio.writef("bitLength(%d) = %d\n", x, width)
    xBinary = dec2bin(x, width)
    stdio.writef("dec2bin(%d) = %s\n", x, xBinary)
    stdio.writef("bin2dec(%s) = %d\n", xBinary, bin2dec(xBinary))


if __name__ == "__main__":
    _main()