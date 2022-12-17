from sys import stdin, stdout

trees = []
for line in stdin:
    letter = [x for x in line.strip()]
    # print(letter)
    trees.append(letter)

for p in range(len(trees)):
    for q in range(len(trees)):
        temp = trees[p][q]
        trees[p][q] = int(temp)


def CheckVis(x, y, trees):
    size = len(trees)
    # if ((x or y) == (0 or (len(trees)-1))):
    #     return True
    north = True
    south = True
    east = True
    west = True
    # check North view

    for i in range(y):
        if (trees[x][i] >= trees[x][y]):
            north = False
        # else:
        #     north = False
        #     break
    # check South view
    for i in range((size-1), y, -1):

        if (trees[x][i] >= trees[x][y]):
            south = False
            # continue
        # else:
        #     south = False
        #     break
    # check West view
    for i in range(x):
        if (trees[i][y] >= trees[x][y]):
            #    continue
            # else:
            west = False
        #    break
    # check East

    for i in range((size-1), x, -1):
        if (trees[i][y] >= trees[x][y]):
            #    continue
            # else:
            east = False
        #    break
    if (north or south or east or west):
        #print(north, south, east, west)
        #print(x, " ", y, trees[x][y])
        return True


total = 0
for j in range(len(trees)):
    for k in range(len(trees)):
        if (CheckVis(j, k, trees)):
            total += 1
print("total: ", total)
