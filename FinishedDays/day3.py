from sys import stdin, stdout

totals = []
for line in stdin:
    totals.append(line)

total = 0
for sack in totals:
    halfway = int(len(sack)/2)
    word_1 = set(sack[:halfway])
    word_2 = set(sack[halfway:])

    letterSet = word_1.intersection(word_2)
    dupl = 'a'
    for i in letterSet:
        dupl = i
    if (ord(dupl) > 96):  # it's lowercase
        total += (ord(dupl) - 96)
    else:
        total += (ord(dupl) - 64) + 26

print(total)
