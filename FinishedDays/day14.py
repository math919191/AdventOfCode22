input = open("input.txt", "r")


def findTheInBetweens(x1, y1, x2, y2):
    newWalls = set()
    if (x1 - x2 == 0):

        if (y1 - y2 >= 0):
            for i in range(y1-y2+1):
                newWalls.add((x1, y1 - i))
        elif (y1 - y2 < 0):
            for i in range(0, abs(y1-y2)+1):
                newWalls.add((x1, y1 + i))

    elif (y1 - y2 == 0):
        if (x1 - x2 >= 0):
            for i in range(x1-x2+1):
                newWalls.add((x1-i, y1))
        elif (x1 - x2 < 0):
            for i in range(0, abs(x1-x2)+1):
                newWalls.add((x1+i, y1))
    return newWalls


def makeFall(x, y, walls, maxY):
    while (True):
        if (y > maxY):
            return False
        # if possible fall down one step
        elif (((x, y+1) in walls) == False):
            y = y + 1
        # elif possible fall down one step and to the left
        elif (((x-1, y+1) in walls) == False):
            x = x - 1
            y = y + 1
        # elif possible fall down one step and to the right
        elif (((x+1, y+1) in walls) == False):
            x = x + 1
            y = y + 1
        else:
            return (x, y)


blocked = set()
maxY = 0
for line in input:
    paths = line.strip().split(" -> ")

    for i in range(len(paths) - 1):
        x1, y1 = paths[i].split(",")
        x2, y2 = paths[i+1].split(",")
        walls = findTheInBetweens(int(x1), int(y1), int(x2), int(y2))
        blocked = blocked | (walls)
        maxY = max(int(y1), int(y2), maxY)

origLen = len(blocked)

while (True):
    settled = makeFall(500, 0, blocked, maxY)
    if (settled == False):
        break
    else:
        blocked.add(settled)
print(len(blocked) - origLen)
# first falls down one step
# then if not possible
#   falls down and to the left
# then if not possible
#   falls down and to the right
