from sys import stdin, stdout
lines = []
for line in stdin:
    lines.append(line.strip())


def getNum(currLine):
    uniqueLetters = 0
    iter = 0
    while (uniqueLetters < 14):
        iter += 1
        uniqueLetters = len(set(currLine[iter:iter+14]))

    print(iter + 14)
    return (iter + 14)


total = 0
for line in lines:
    total += getNum(line)

print(total)
