
input = open("input.txt", "r")

doneReadingMap = False
map = []
dirString = ""
directions = []

dirs = {0: "R", 1: "D", 2: "L", 3: "U"}
undoDir = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}

maxLen = 0

for line in input:
    maxLen = max(maxLen, len(line))
    if (line != "\n" and doneReadingMap == False):
        row = [x for x in line]
        row.insert(0, " ")
        row.append(" ")
        map.append(row)
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


def getEdges():
    edges = dict()
    edges["1to2"] = "normal"
    edges["1to6"] = "normal"
    edges["1to4"] = ""  # map[151][50-99] / [3][1-2]
    edges["1to5"] = ""  # map[100-150][100] / [1-2][]

    edges["2to1"] = "normal"
    edges["2to3"] = "normal"
    edges["2to5"] = ""
    edges["2to6"] = ""

    edges["3to2"] = "normal"
    edges["3to5"] = ""
    edges["3to6"] = ""
    edges["3to4"] = ""  # map[1][50-99] / [0][1-2]

    edges["4to1"] = ""
    edges["4to3"] = ""
    edges["4to5"] = ""
    edges["4to6"] = "normal"

    edges["5to1"] = ""
    edges["5to2"] = ""
    edges["5to4"] = ""  # map[1][100-149] / [0][2-3]
    edges["5to3"] = "normal"

    edges["6to1"] = "normal"
    edges["6to2"] = ""  # map[100][0-49] / [2][0-1]
    edges["6to4"] = "normal"
    edges["6to3"] = ""


def makeEdges():
    edges = dict()
    #   0 1 2 3 (second)
    # 0   X 5
    # 1   2
    # 2 X X
    # 3 X
    # (first)

    # to go from an edge 2 to 5 -- pivot
    # you can also do this for
    # - 2 / 5
    # - 2 / 6
    # - 1 / 4
    # you can do
    #  toAdd = (start - pivot).reverse()
    #  end = pivot + toAdd

    edges["2to5"] = dict()
    edges["2to5"]["coor"] = {"row": 1, "column": 1.5}
    edges["2to5"]["mapcoor"] = {"row": [51, 100], "column": 100}
    edges["2to5"]["rule"] = "coor"

    edges["5to2"] = dict()
    edges["5to2"]["coor"] = {"row": .5, "column": 2}
    edges["5to2"]["mapcoor"] = {"row": 50, "column": [51, 100]}


def getEdgeNum(cord):
    # I swapped them here because it's confusing
    y = cord[0] - 1
    x = cord[1] - 1

    edgeLen = 50
    # these are the horizontal edges
    if ((edgeLen*1 < x < edgeLen*2) and y == 0):
        return "3to4"
    elif ((edgeLen*2 < x < edgeLen*3) and y == 0):
        return "5to4"
    elif ((edgeLen*0 < x < edgeLen*1) and y == edgeLen*2):
        return "6to2"
    elif ((edgeLen*0 < x < edgeLen*1) and y == edgeLen*4):
        return "4to5"
    elif ((edgeLen*1 < x < edgeLen*2) and y == edgeLen*3):
        return "1to4"
    elif ((edgeLen*2 < x < edgeLen*3) and y == edgeLen*1):
        return "5to2"
    # verticle edges
    elif (x == 0 and (edgeLen*2 < y < edgeLen*3)):
        return "6to3"
    elif (x == 0 and (edgeLen*3 < y < edgeLen*4)):
        return "4to3"
    elif (x == edgeLen*1 and (edgeLen*0 < y < edgeLen*1)):
        return "3to6"
    elif (x == edgeLen*1 and (edgeLen*1 < y < edgeLen*2)):
        return "2to6"
    elif (x == edgeLen*2 and (edgeLen*1 < y < edgeLen*2)):
        return "2to5"
    elif (x == edgeLen*2 and (edgeLen*2 < y < edgeLen*3)):
        return "1to5"
    else:
        print("ERROR from getEdgeNum!")
        return "ERROR"


def addList(list1, list2):
    return [list1[x] + list2[x] for x in range(len(list1))]


def subList(list1, list2):
    return [list1[x] - list2[x] for x in range(len(list1))]


def flop(list1):
    return [list1[1], list1[0]]


def getPivot(edgeNum):
    if (edgeNum == "2to6" or edgeNum == "6to2"):
        return [101, 51]
    elif (edgeNum == "2to5" or edgeNum == "5to2"):
        return [51, 101]
    elif (edgeNum == "4to1" or edgeNum == "1to4"):
        return [151, 51]
    # other case for 4 to 5


def pivotMove(coor, edgeNum):
    pivot = getPivot(edgeNum)
    flop = flop(subList(coor, pivot))
    b = addList(pivot, flop)
    return b


def moveAroundCube(coor, edgeNum):
    if (edgeNum == "2to6" or edgeNum == "6to2" or
        edgeNum == "2to5" or edgeNum == "5to2" or
        edgeNum == "4to1" or edgeNum == "1to4"
        ):
        return pivotMove(coor, edgeNum)
    elif (edgeNum == "3to6" or edgeNum == "6to3"):
        if (edgeNum == "3to6"):
            coor[0] = coor[0] - 50
            coor[1] = 150 - coor[1]
            return coor
        else:
            coor[0] = coor[0] + 50
            coor[1] = 150 - coor[1]
            return coor
    elif (edgeNum == "4to5" or edgeNum == "5to4"):
        if (edgeNum == "4to5"):
            coor[0] = coor[0] + 100
            coor[1] = coor[1] - 200
            return coor
        else:
            coor[0] = coor[0] - 100
            coor[1] = coor[1] + 200
            return coor
    elif ()


def wrapCoorIfNeededPart2(dir, coor):
    if (map[coor[0]][coor[1]] != " "):
        return coor  # it doesn't need wrapped
    backUp = coor + undoDir[dir]
    edgeNum = getEdgeNum(backUp)


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
# 1484 is right
