
input = open("input.txt", "r")

doneReadingMap = False
map = []
dirString = ""
directions = []

dirs = {0: "R", 1: "D", 2: "L", 3: "U"}
maxLen = 0

for line in input:
    maxLen = max(maxLen, len(line))
    if (line != "\n" and doneReadingMap == False):
        map.append([x for x in line])
    else:
        doneReadingMap = True
        dirString = dirString + line

for row in map:
    row[-1] = " "  # replacing all the newlines with " "
    for i in range(maxLen - len(row) + 1):
        row.append(" ")

spaces = [" " for x in range(len(map[0])+1)]
map.insert(0, spaces)
map.append(spaces)


num = ""
for c in dirString:
    if (c == "L" or c == "R"):
        directions.append(int(num))
        directions.append(c)
        num = ""
    else:
        num = num + c
directions.append(int(num))


def incrementOne(dir, mycoor):
    if (dir == 0):
        mycoor[1] = mycoor[1] + 1
    elif (dir == 1):
        mycoor[0] = mycoor[0] + 1
    elif (dir == 2):
        mycoor[1] = mycoor[1] - 1
    elif (dir == 3):
        mycoor[0] = mycoor[0] - 1
    return mycoor


def wrapCoorIfNeeded(dir, coor):
    if (map[coor[0]][coor[1]] != " "):
        return coor  # it doesn't need wrapped
    if (dir == 0 or dir == 2):  # Left and right
        howFarToJump = 0
        for i in range(len(map[coor[0]])):
            if (map[coor[0]][i] != " "):
                howFarToJump += 1
        coor[1] = coor[1] + (dir - 1) * howFarToJump
        return coor
    elif (dir == 3):  # it was going up
        counter = 1
        while (map[coor[0] + counter][coor[1]] != " "):
            counter += 1
        coor[0] = coor[0] + counter - 1
        return coor
    elif (dir == 1):  # it was going down
        counter = -1
        while (map[coor[0] + counter][coor[1]] != " "):
            counter -= 1
        coor[0] = coor[0] + counter + 1
        return coor


def hitsWall(dir, myCoor):
    myCoor = incrementOne(dir, myCoor)
    myCoor = wrapCoorIfNeeded(dir, myCoor)
    # check if hitting wall or is out of range
    if (map[myCoor[0]][myCoor[1]] == "#"):
        return True
    else:
        return False


def move(steps, dir, coor):
    origCoor = coor.copy()
    for i in range(steps):
        coorToTest = coor.copy()
        if (hitsWall(dir, coorToTest)):
            break
        coor = incrementOne(dir, coor)
        coor = wrapCoorIfNeeded(dir, coor)

    # checks if it has moved for the facing
    if (origCoor == coor):
        return False
    else:
        return True


def rotate(dirToRotate, currDir):
    if (dirToRotate == "R"):
        return (currDir + 1) % 4
    elif (dirToRotate == "L"):
        return (currDir - 1) % 4


def getStartingPos():
    starting = [1, 0]
    for x in range(len(map)):
        if (map[1][x] == "."):
            starting[1] = x
            return starting


# starts
# leftmost open tile of the top row of tiles.
# to the right


currDir = 0
facing = currDir + 0
coor = getStartingPos()

for instruction in directions:
    if (instruction == "R" or instruction == "L"):
        # instruction is the direction
        currDir = rotate(instruction, currDir)
    else:
        # instruction is the number of steps
        moved = move(instruction, currDir, coor)
        facing = currDir + 0

row = coor[0]
col = coor[1]

answer = (row * 1000 + (col+1) * 4 + currDir)
print("Part 1:", answer)

# 1388 is too low
