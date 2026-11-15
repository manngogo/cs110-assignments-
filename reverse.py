import stdio #importing to use code

# Read all strings from standard input into a list
a = stdio.readAllStrings()
n = len(a)

# Reverse the list in place by swapping mirrored elements
for i in range(n // 2):
    a[i], a[n - i - 1] = a[n - i - 1], a[i]

# Write the reversed strings, separated by spaces
for i in range(n):
    if i < n - 1:
        stdio.write(f'{a[i]} ')
    else:
        stdio.write(f'{a[i]}\n')