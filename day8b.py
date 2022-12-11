from sys import stdin, stdout

trees = []
for line in stdin:
    letter = [x for x in line.strip()]
    # print(letter)
    letter.insert(0, 9)
    letter.append(9)
    trees.append(letter)

nines = []
for n in range(len(trees[0])):
    nines.append(9)
trees.insert(0, nines)
trees.append(nines)


for p in range(len(trees)):
    for q in range(len(trees)):
        temp = trees[p][q]
        trees[p][q] = int(temp)
for i in trees:
    print(i)


def CheckVis(x, y, trees):
    size = len(trees)
    print(trees[x][y])
    north = True
    south = True
    east = True
    west = True
    northCount = 1
    southCount = 1
    westCount = 1
    eastCount = 1
    # check North view
    # and (0 < (y + northCount) < (size-1))
    #print(trees[x][y], trees[x][y + northCount])
    while ((trees[x][y] > trees[x][y + northCount]) and (0 < (y + northCount) < (size-1))):
        print(trees[x][y], trees[x][y + northCount])
        print("nc", northCount)
        print("coor: ", x, y + northCount)
        print("trees at coor:", trees[x][y+northCount])
        northCount += 1
    while ((trees[x][y] > trees[x][y - southCount]) and (0 < (y - southCount) < (size-1))):
        southCount += 1
    while ((trees[x][y] > trees[x + westCount][y]) and (0 < (x + westCount) < (size-1))):
        westCount += 1
    while ((trees[x][y] > trees[x - eastCount][y]) and (0 < (x - eastCount) < (size-1))):
        eastCount += 1

    print(northCount, southCount, eastCount, westCount)
    return northCount * southCount * westCount * eastCount


total = 0
max = 0


count = CheckVis(3, 2, trees)
print(count)
# for j in range(1, len(trees)-1):
#     for k in range(1, len(trees)-1):
#         count = CheckVis(j, k, trees)
#         if (count > max):
#             max = count
# total += 1
# print("total: ", max)
