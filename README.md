# RSA Cryptosystem
 
Python programs that implement the RSA public-key cryptosystem: a library for generating keys and encrypting and decrypting integers, plus command-line programs that generate keys and encrypt and decrypt text.
 
## Requirements
 
- Python 3
- The course `std*` libraries (`stdio`, `stdarray`, `stdrandom`) on your Python path
- A `data/` folder with sample texts (`adams.txt`, `buddha.txt`, `darwin.txt`, `einstein.txt`)
Run every command below from this folder.
 
## Using RSA (Part II)
 
### keygen.py
Takes `lo` and `hi` and writes a public/private key as `n e d`, separated by spaces. The two primes used to build the key are picked at random from `[lo, hi)`, so the output changes each run.
 
```
$ python3 keygen.py 50 100
3599 1759 2839
```
 
- The **public key** is `(n, e)`.
- The **private key** is `(n, d)`.
### encrypt.py
Takes the public key `n` and `e` as command-line arguments, reads a message from standard input, and writes each character encrypted as a fixed-width binary number. Choose `n` greater than 127 so every ASCII character fits.
 
```
$ python3 encrypt.py 3599 1759
CS110
<ctrl-d>
```
 
Note that pressing Enter before Ctrl-D adds a newline character to the message, which is encrypted too.
 
### decrypt.py
Takes the private key `n` and `d` as command-line arguments, reads the binary output of `encrypt.py` from standard input, and writes the original message.
 
```
$ python3 decrypt.py 3599 2839
<paste the binary output of encrypt.py, then ctrl-d>
CS110
```
 
### Encrypt and decrypt together
Use the same `n` with the matching `e` and `d`:
 
```
$ python3 keygen.py 50 100
5963 4447 367
$ python3 encrypt.py 5963 4447 < data/adams.txt | python3 decrypt.py 5963 367
```
 
This prints the original text of `data/adams.txt`.
 
### rsa.py
The library behind the three programs above. Import it with `import rsa`.
 
| Function | Description |
|---|---|
| `keygen(lo, hi)` | Returns the keys as a tuple `(n, e, d)`, picking primes from `[lo, hi)` |
| `encrypt(x, n, e)` | Encrypts the integer `x` with the public key `(n, e)` |
| `decrypt(y, n, d)` | Decrypts the integer `y` with the private key `(n, d)` |
| `bitLength(n)` | Returns the least number of bits needed to represent `n` |
| `dec2bin(n, width)` | Returns `n` in binary, padded with leading zeros to `width` |
| `bin2dec(n)` | Returns the decimal value of the binary string `n` |
 
Running `rsa.py` on its own with one character runs a quick self-test (keys are random, so the encrypted number varies):
 
```
$ python3 rsa.py S
encrypt(S) = 1743
decrypt(1743) = S
bitLength(83) = 7
dec2bin(83) = 1010011
bin2dec(1010011) = 83
```
 
## Warmup programs (Part I)
 
### reverse.py
Reads strings from standard input and writes them in reverse order.
 
```
$ python3 reverse.py
b o l t o n
<ctrl-d>
n o t l o b
```
 
### distance.py
Takes `n` as a command-line argument, reads two vectors of `n` numbers from standard input, and writes the Euclidean distance between them.
 
```
$ python3 distance.py 5
-9 1 10 -1 1
-5 9 6 7 4
13.0
```
 
### transpose.py
Takes `m` (rows) and `n` (columns) as command-line arguments, reads an m-by-n matrix from standard input, and writes its transpose.
 
```
$ python3 transpose.py 2 3
1 2 3
4 5 6
1.0 4.0
2.0 5.0
3.0 6.0
```
 
### palindrome.py
Takes a lowercase string with no spaces as a command-line argument and writes `True` if it reads the same forwards and backwards, `False` otherwise.
 
```
$ python3 palindrome.py amanaplanacanalpanama
True
```
 
### sin.py
Takes an angle in degrees as a command-line argument and writes its sine, calculated with the Taylor series.
 
```
$ python3 sin.py 60
0.8660254037844385
```