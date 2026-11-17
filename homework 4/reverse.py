import stdio

# this program reads a list of strings from standard input and writes them back out in reverse order. 
# main() below reads the strings into a list, calls our _reverse() function to reverse that list in place, then writes the strings
# one after another, each followed by a space.
# Entry point (DO NOT EDIT).
def main():
    a = stdio.readAllStrings()
    _reverse(a)
    for v in a:
        stdio.writef("%s ", v)
    stdio.writeln()

# Reverses a in place without creating a new list.
def _reverse(a):
    # Step 1: find out how many strings are in the list. We use this to work out which
    # position is the "mirror" of each position (position i mirrors position n - 1 - i).
    n = len(a)
    
    # Step 2: swap each pair of mirrored entries, working inwards from both ends.
    # We only need to visit the FIRST HALF of the positions: every swap fixes two entries
    # at once (the one at i and the one at n - 1 - i). If we looped over all n positions,
    # every pair would be swapped twice and the list would end up exactly as it started.
    # n // 2 rounds down, so for a list with an odd number of entries the middle entry is
    # never touched, which is correct because it is already in its final position in the middle
    for i in range(n // 2):
        # Swap a[i] with its mirror. Python evaluates the entire right-hand side first
        # and only then assigns, so we do not need a temporary variable to hold a value.
        a[i], a[n - 1 - i] = a[n - 1 - i], a[i]


if __name__ == "__main__":
    main()
