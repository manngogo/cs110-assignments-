import stdio
import sys
n = int(sys.argv[1])
# The dragon curve starts at order 0 as a single forward step, represented by the letter 'F'.
# Order 0 curve is a single forward step
dragon = 'F'
# Repeat the generation process once for new inputs
for _ in range(n):
    # Create a new string that is the reverse of the current curve, while swapping L and R turns.
    reversed_swapped = ''
    # Traverse the current curve from the end to the beginning so the reverse is built correctly.
    for i in range(len(dragon) - 1, -1, -1):
        c = dragon[i]
        # If the current instruction is 'L', change it to 'R' in the reversed copy.
        if c == 'L':
            reversed_swapped += 'R'
        # If the current instruction is 'R', change it to 'L' in the reversed copy.
        elif c == 'R':
            reversed_swapped += 'L'
        # A forward step stays the same because it is not a turn.
        else:
            reversed_swapped += 'F'

    # Build the next order by taking the current curve, adding an 'L', and then appending the reversed/swapped version.
    # Order k = order (k-1) + 'L' + reversed/swapped order (k-1)
    dragon = dragon + 'L' + reversed_swapped
#Print the final result
stdio.writeln(dragon)