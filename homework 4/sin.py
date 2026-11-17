import math
import stdio
import sys

# this program reads an angle in degrees from the command line, converts it to radians, and writes its sine, 
# which is calculated by our _sin() function using the series  sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
# Entry point (DO NOT EDIT).

def main():
    x = float(sys.argv[1])
    stdio.writeln(_sin(math.radians(x)))

# Returns sin(x) calculated using the formula: sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...

def _sin(x):
    # Step 1: bring x into the range [-pi, pi]. The sine repeats every 2*pi, so subtracting whole turns doesnt change the 
    # answer, but it keeps x small. The series is very accurate for small x and loses accuracy for large angles (like 1000 degrees).
    # First reduce x to [-pi, pi] to keep the series accurate for large arguments.
    x = x % (2 * math.pi)
    if x > math.pi:
        x -= 2 * math.pi

    # Step 2: start the sum with the first term of the series, which is just x.
    # term holds the current term, and total holds the sum of all terms so far.
    term = x
    total = x

    # k counts which term we are about to add 
    k = 1

    # Step 3: keep adding terms until adding another one no longer changes the sum.
    while True:
        # Build the next term from the previous one 
        term = -term * x * x / ((2 * k) * (2 * k + 1))

        # Add the new term to a copy of the total so we can see whether it made a difference.
        new_total = total + term

        # The terms shrink toward zero. Once a term is so small that adding it changes nothing (because floats only keep about 16 digits), 
        # we are as accurate as possible and can stop.
        if new_total == total:
            break

        # Otherwise keep the new sum and move on to the next term.
        total = new_total
        k += 1

    # Step 4: the sum is our approximation of sin(x).
    return total


if __name__ == "__main__":
    main()
