from sys import stdin, stdout

count = 0
maxHeight = 0
totals = []
for line in stdin:
    totals.append(line)
    count += 1
    if (line == '\n'):
        maxHeight = count - 1
numStacks = (len(totals[0]) + 1) // 4

stacks = []
for i in range(numStacks):
    stacks.append([])

for i in range(maxHeight - 1):
    line = totals[i]
    for stackNum in range(numStacks):
        index = stackNum*4 + 1
        blockLetter = line[index]

        if (blockLetter != " "):
            stacks[stackNum].append(blockLetter)


for k in range(maxHeight+1, len(totals)):
    line = totals[k]
    move, count, fr, start, to, end = line.split(' ')
    count = int(count)
    start = int(start) - 1  # 0 based indexing
    end = int(end) - 1  # 0 based indexing

    for i in range(int(count)):
        movingBox = stacks[start][0]
        stacks[start].pop(0)
        stacks[end].insert(0, movingBox)

# for xs in stacks:
#     print(" ".join(map(str, xs)))

for i in range(len(stacks)):
    print(stacks[i][0], end='')
