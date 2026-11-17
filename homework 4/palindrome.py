import stdio
import sys


# this program reads a string from the command line and writes True if it is a palindrome and False otherwise. 
# main() below reads the string and writes the answer from our _isPalindrome() function.
# Entry point (DO NOT EDIT).
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))

# Returns True if s is a palindrome and False otherwise.
def _isPalindrome(s):
    # Step 1: find the length of the string. The character at position i has its mirror
    # at position n - 1 - i (for example, in "madam" position 0 mirrors position 4).
    n = len(s)

    # Step 2: compare each character in the first half of the string with its mirror. We stop at the middle (n // 2) because the 
    # second half would just repeat the same comparisons. For an odd length the middle character has nothing to compare with,
    # and that is fine. This also works for a one-letter string and an empty string, bc the loop just doesnt run.
    for i in range(n // 2):
        # Compare this character with its mirror.
        if s[i] != s[n - 1 - i]:
            # One mismatch is enough to know it is not a palindrome, so we can stop now.
            return False

    # Step 3: we only reach this line if EVERY pair matched (this return is deliberately after the loop; putting it inside the loop would 
    # stop after checking only the first pair).
    return True


if __name__ == "__main__":
    main()