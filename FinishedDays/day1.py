# cmd /c 'py day1.py < input.txt > output.txt'
from sys import stdin, stdout

counter = 0
totals = []
for line in stdin:
    if (line != "\n"):
        counter += int(line)
    else:
        totals.append(counter)
        counter = 0
totals.sort(reverse=True)
print("Part 1: ", totals[0])
print("Part 2: ", totals[0] + totals[1] + totals[2])
