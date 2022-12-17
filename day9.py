import copy
f = open("input.txt", "r")

directions = []
for line in f:
    a, b = line.split(" ")
    directions.append([a, int(b)])

visited = []
t = [0, 0]
h = [0, 0]
oldH = h

r = []  # r for rope
for i in range(10):
    r.append([0, 0])


def checkAdj(t, h):
    if (abs(t[0]-h[0]) <= 1 and abs(t[1]-h[1]) <= 1):
        return True
    else:
        return False


def stringifyT(t):
    return str(t[0]) + "," + str(t[1])


def checkDiagonal(t, h):
    if (abs(t[0]-h[0]) == 2 and abs(t[1]-h[1] == 1)):
        return True
    elif (abs(t[0]-h[0]) == 1 and abs(t[1]-h[1] == 2)):
        return True
    else:
        return False


def checkPositive(x, y):
    if (x - y > 0):
        return 1
    else:
        return -1


def moveKnot(oldLead, lead, follow):
    newKnot = follow
    dif0 = lead[0] - follow[0]
    dif1 = lead[1] - follow[1]
    if (dif0 == 2):
        newKnot[0] = newKnot[0]+1
    if (dif1 == 2):
        newKnot[1] = newKnot[1]+1
    if (dif0 == -2):
        newKnot[0] = newKnot[0]-1
    if (dif1 == -2):
        newKnot[1] = newKnot[1]-1

    if (abs(dif0) + abs(dif1) == 3):
        if (dif0 == 1):
            newKnot[0] = newKnot[0]+1
        elif (dif1 == 1):
            newKnot[1] = newKnot[1]+1
        elif (dif0 == -1):
            newKnot[0] = newKnot[0]-1
        elif (dif1 == -1):
            newKnot[1] = newKnot[1]-1

    return newKnot
    # if (checkAdj(follow, lead) == False):
    #     if (checkDiagonal(follow, lead)):
    #         follow[0] += (checkPositive(follow[0], lead[0]))
    #         follow[1] += (checkPositive(follow[1], lead[1]))
    #         return follow
    #     follow = oldLead
    #     return oldLead
    # else:
    #     return follow


def printRope(rope):
    map = []
    newlist = ["." for x in range(6)]
    map = [copy.deepcopy(newlist) for x in range(6)]

    count = 0
    for i in rope:
        map[len(map)-(i[1])-1][i[0]] = count
        count += 1
    for x in map:
        for y in x:
            print(y, end="")
        print("")


for d in directions:
    for i in range(d[1]):
        oldHead = [r[0], r[1]]
        oldR = copy.deepcopy(r)
        if (d[0] == "R"):
            r[0][0] = r[0][0] + 1
        elif (d[0] == "L"):
            r[0][0] = r[0][0] - 1
        elif (d[0] == "D"):
            r[0][1] = r[0][1] - 1
        elif (d[0] == "U"):
            r[0][1] = r[0][1] + 1

        for k in range(len(r)-1):
            newKnot = moveKnot(oldR[k], r[k], oldR[k+1])
            r[k + 1] = newKnot
        visited.append(stringifyT(r[-1]))
        # printRope(r)
        # print(r)

# print(visited)
mySet = set(visited)
# print(mySet)
print(len(visited), len(mySet))

# 9040 too high
# 6493 too low
# needed to add one
