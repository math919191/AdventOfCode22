from sys import stdin, stdout

totals = []
for line in stdin:
    totals.append(line)

total = 0
let = []
groups = int(len(totals)/3)
for i in range(groups):
    b1 = set(totals[i*3])
    b2 = set(totals[i*3 + 1])
    b3 = set(totals[i*3 + 2])

    letterSet = b3.intersection(b1.intersection(b2))
    dupl = 'a'
    for j in letterSet:
        if (j != (' ') and j != '\n'):
            dupl = j
            let.append(dupl)
    if (ord(dupl) > 96):  # it's lowercase
        total += (ord(dupl) - 96)
    else:
        total += ((ord(dupl) - 64) + 26)
print(total)
