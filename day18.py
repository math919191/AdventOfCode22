input = open("input.txt", "r")
map = []
size = 23  # 24 for full input

for x in range(size):
    xMap = []
    for y in range(size):
        xMap.append([])
        for z in range(size):
            xMap[y].append(False)
    map.append(xMap)

# 5,7,4
for line in input:
    coor = line.split(",")
    coor = [int(x) for x in coor]
    map[coor[0]][coor[1]][coor[2]] = True


def checkNumOfFreeSides(map, coor):
    total = 0
    if (map[coor[0]-1][coor[1]][coor[2]] == False):
        total += 1
    if (map[coor[0]+1][coor[1]][coor[2]] == False):
        total += 1
    if (map[coor[0]][coor[1]-1][coor[2]] == False):
        total += 1
    if (map[coor[0]][coor[1]+1][coor[2]] == False):
        total += 1
    if (map[coor[0]][coor[1]][coor[2]+1] == False):
        total += 1
    if (map[coor[0]][coor[1]][coor[2]-1] == False):
        total += 1
    return total


def checkNumOfOutsideFreeSides(map, coor):
    total = 0
    if (map[coor[0]-1][coor[1]][coor[2]] == "outside"):
        total += 1
    if (map[coor[0]+1][coor[1]][coor[2]] == "outside"):
        total += 1
    if (map[coor[0]][coor[1]-1][coor[2]] == "outside"):
        total += 1
    if (map[coor[0]][coor[1]+1][coor[2]] == "outside"):
        total += 1
    if (map[coor[0]][coor[1]][coor[2]+1] == "outside"):
        total += 1
    if (map[coor[0]][coor[1]][coor[2]-1] == "outside"):
        total += 1
    return total


def checkBounds(num):
    if (num >= 0 and num < (size-1)):
        return True
    else:
        return False


def greedilyFillOutside(map, x, y, z):
    # check bounds
    if (checkBounds(x) and checkBounds(y) and checkBounds(z)):
        pass
    else:
        return map

    # check if already touching outsides
    if (map[x][y][z] == "outside"):
        if (map[x+1][y][z] == False):
            map[x+1][y][z] = "outside"
            greedilyFillOutside(map, x+1, y, z)
        if (map[x-1][y][z] == False):
            map[x-1][y][z] = "outside"
            greedilyFillOutside(map, x-1, y, z)
        if (map[x][y+1][z] == False):
            map[x][y+1][z] = "outside"
            greedilyFillOutside(map, x, y+1, z)
        if (map[x][y-1][z] == False):
            map[x][y-1][z] = "outside"
            greedilyFillOutside(map, x, y-1, z)
        if (map[x][y][z+1] == False):
            map[x][y][z+1] = "outside"
            greedilyFillOutside(map, x, y, z+1)
        if (map[x][y][z-1] == False):
            map[x][y][z-1] = "outside"
            greedilyFillOutside(map, x, y, z-1)

    else:
        return map


map[0][0][0] = "outside"
greedilyFillOutside(map, 0, 0, 0)

answer = 0
for x in range(size-1):
    for y in range(size-1):
        for z in range(size-1):
            if (map[x][y][z] == True):
                answer += checkNumOfOutsideFreeSides(map, [x, y, z])
                # print(x, y, z)
                # print(answer)
                #answer += checkNumOfFreeSides(map, [x, y, z])

print(answer)

# 4454 is too low
