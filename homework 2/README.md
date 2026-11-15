# Homework 2
 
Command-line programs that use loops, conditionals and a little number theory.
 
## Requirements
 
- Python 3
- The course `stdio` and `stdrandom` libraries on your Python path
Run every command from this folder. Inputs are given as command-line arguments.
 
## Random programs
 
### card.py
Takes no arguments and writes a random playing card.
 
```
$ python3 card.py
9 of Diamonds
```
 
### die_roll.py
Takes the number of sides `n` and writes the sum of two random rolls of an n-sided die.
 
```
$ python3 die_roll.py 6
7
```
 
Both programs give different output each run.
 
## Calendar and geometry
 
### day_of_week.py
Takes a month, day and year (`m d y`) and writes the day of the week.
 
```
$ python3 day_of_week.py 11 14 2026
Saturday
```
 
### dragon_curve.py
Takes an order `n` and writes the dragon curve of that order as a string of `F` (forward), `L` (left turn) and `R` (right turn).
 
```
$ python3 dragon_curve.py 3
FLFLFRFLFLFRFRF
```
 
## Sequences and number theory
 
### factorial.py
Takes `n` and writes `n!`.
 
```
$ python3 factorial.py 5
120
```
 
### fibonacci.py
Takes `n` and writes the nth Fibonacci number (F(0) = 0, F(1) = 1).
 
```
$ python3 fibonacci.py 10
55
```
 
### gcd.py
Takes two integers and writes their greatest common divisor, using the Euclidean algorithm.
 
```
$ python3 gcd.py 48 18
6
```
 
### primality_test.py
Takes `n` and writes `True` if it is prime, `False` otherwise.
 
```
$ python3 primality_test.py 97
True
```
 
### prime_counter.py
Takes `n` and writes how many primes are less than or equal to `n`.
 
```
$ python3 prime_counter.py 100
25
```
 
### perfect_numbers.py
Takes `n` and writes every perfect number up to `n`, one per line.
 
```
$ python3 perfect_numbers.py 500
6
28
496
```
 
### ramanujan_numbers.py
Takes `n` and writes every number up to `n` that can be written as a sum of two positive cubes in two different ways.
 
```
$ python3 ramanujan_numbers.py 5000
1729 = 1^3 + 12^3 = 9^3 + 10^3
4104 = 2^3 + 16^3 = 9^3 + 15^3
```
 
### sum_of_powers.py
Takes `n` and `k` and writes 1^k + 2^k + ... + n^k.
 
```
$ python3 sum_of_powers.py 5 2
55
```
 
## Equations
 
### quadratic.py
Takes the coefficients `a b c` of a quadratic equation and writes its two roots. It prints an error message and exits if `a` is 0 or the discriminant is negative.
 
```
$ python3 quadratic.py 1 -3 2
 2.0 1.0
$ python3 quadratic.py 0 1 1
Value of a must not be 0
```
 
### root.py
Takes `k`, `c` and a tolerance `epsilon`, and writes the kth root of `c`, found with Newton's method.
 
```
$ python3 root.py 3 27 1e-9
3.0
```
 
### wind_chill.py
Takes a temperature `t` in degrees Fahrenheit (at most 50) and a wind speed `v` in miles per hour (more than 3) and writes the wind chill. It prints an error message and exits if either is out of range.
 
```
$ python3 wind_chill.py 32 15
21.588988890532022
$ python3 wind_chill.py 60 15
Value of t must be <= 50 F
```