from sys import stdin, stdout

trees = []
for line in stdin:
    nums = [int(x) for x in line.strip()]
    trees.append(nums)


def CheckIfLower(x, y, height):
    if (x <= 0 or x >= (len(trees)-1) or y <= 0 or y >= (len(trees)-1)):
        return False
    if (int(trees[x][y]) < int(height)):
        #print(trees[x][y], height, "true")

        return True
    else:
        return False


def GetScenicScore(x, y):
    treeHeight = trees[x][y]
    #print("treeheight", trees[x][y])
    scores = []
    # check x up
    diff = 1
    while (CheckIfLower(x+diff, y, treeHeight)):
        diff += 1
    scores.append(diff)
    # check x down
    diff = 1
    while (CheckIfLower(x-diff, y, treeHeight)):
        diff += 1

    scores.append(diff)
    # check y up
    diff = 1
    while (CheckIfLower(x, y+diff, treeHeight)):
        diff += 1
    scores.append(diff)
    # check y down
    diff = 1
    while (CheckIfLower(x, y-diff, treeHeight)):
        diff += 1
    scores.append(diff)

    total = 1
    for score in scores:
        total = total * score
    return total


max = 0

for i in range(1, len(trees)-1):
    for j in range(1, len(trees)-1):
        currScore = GetScenicScore(i, j)
        if (currScore > max):
            max = currScore
            # print(max)

print(max)
