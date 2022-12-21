from collections import deque

input = open("input.txt", "r")
map = []
size = 24  # 24 for full input
outside = "NO"

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
    if (map[coor[0]-1][coor[1]][coor[2]] == outside):
        total += 1
    if (map[coor[0]+1][coor[1]][coor[2]] == outside):
        total += 1
    if (map[coor[0]][coor[1]-1][coor[2]] == outside):
        total += 1
    if (map[coor[0]][coor[1]+1][coor[2]] == outside):
        total += 1
    if (map[coor[0]][coor[1]][coor[2]+1] == outside):
        total += 1
    if (map[coor[0]][coor[1]][coor[2]-1] == outside):
        total += 1
    return total


def checkBounds(num):
    if (num >= 0 and num < (size)):
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


def checkIfOutSide(coor):
    if (map[coor[0]][coor[1]][coor[2]] == True):
        return False
    # else:
    #     return True

    if (map[coor[0]-1][coor[1]][coor[2]] == outside):
        return True
    elif (map[coor[0]+1][coor[1]][coor[2]] == outside):
        return True
    elif (map[coor[0]][coor[1]-1][coor[2]] == outside):
        return True
    elif (map[coor[0]][coor[1]+1][coor[2]] == outside):
        return True
    elif (map[coor[0]][coor[1]][coor[2]+1] == outside):
        return True
    elif (map[coor[0]][coor[1]][coor[2]-1] == outside):
        return True
    else:
        return False


def fillOutside(map):
    for i in range(size):
        for j in range(size):
            map[i][j][size-1] = outside
            map[i][j][0] = outside
            map[i][size-1][j] = outside
            map[i][0][j] = outside
            map[size-1][i][j] = outside
            map[0][i][j] = outside

    changes = True
    while (changes):
        changes = False
        for x in range(1, size-1):
            for y in range(1, size-1):
                for z in range(1, size-1):
                    if (map[x][y][z] == False):
                        if (checkIfOutSide([x, y, z])):
                            map[x][y][z] = outside
                            changes = True


def seeIfAllAroundTrue(x, y, z):
    if (map[x+1][y][z]
        and map[x-1][y][z]
        and map[x][y+1][z]
        and map[x][y-1][z]
        and map[x][y][z+1]
            and map[x][y][z-1]):
        return True
    else:
        return False


def check_validity(x, y, z, seen):
    if ((x, y, z) in seen):
        return False

    if (checkBounds(x) and checkBounds(y) and checkBounds(z)
            and (map[x][y][z] != True) and (map[x][y][z] != outside)):
        return True
    else:
        return False


def flood_fill(x, y, z):
   # here check_validity is a function that given coordinates of the point tells you whether
   # the point should be colored or not
    seen = set()
    q = deque()
    q.append((x, y, z))
    while (len(q) != 0):  # It is not empty
        (x1, y1, z1) = q.popleft()
        # color(x1,y1,z1)
        map[x1][y1][z1] = outside
        if (check_validity(x1+1, y1, z1, seen)):
            q.append((x1+1, y1, z1))
            seen.add((x1+1, y1, z1))
        if (check_validity(x1-1, y1, z1, seen)):
            q.append((x1-1, y1, z1))
            seen.add((x1-1, y1, z1))
        if (check_validity(x1, y1+1, z1, seen)):
            q.append((x1, y1+1, z1))
            seen.add((x1, y1+1, z1))
        if (check_validity(x1, y1-1, z1, seen)):
            q.append((x1, y1-1, z1))
            seen.add((x1, y1-1, z1))
        if (check_validity(x1, y1, z1+1, seen)):
            q.append((x1, y1, z1+1))
            seen.add((x1, y1, z1+1))
        if (check_validity(x1, y1, z1-1, seen)):
            q.append((x1, y1, z1-1))
            seen.add((x1, y1, z1-1))
    print("finished")


def checkNumOfInsideSurface(map, coor):
    total = 0
    if (map[coor[0]-1][coor[1]][coor[2]] == True):
        total += 1
    if (map[coor[0]+1][coor[1]][coor[2]] == True):
        total += 1
    if (map[coor[0]][coor[1]-1][coor[2]] == True):
        total += 1
    if (map[coor[0]][coor[1]+1][coor[2]] == True):
        total += 1
    if (map[coor[0]][coor[1]][coor[2]+1] == True):
        total += 1
    if (map[coor[0]][coor[1]][coor[2]-1] == True):
        total += 1
    return total


# map[0][0][0] = "outside"
# greedilyFillOutside(map, 0, 0, 0)
# fillOutside(map)
flood_fill(0, 0, 0)
print("flood filled")

answer = 0
answer2 = 0
for x in range(size-1):
    for y in range(size-1):
        for z in range(size-1):
            if (map[x][y][z] == False):
                answer += checkNumOfInsideSurface(map, [x, y, z])
            # if (map[x][y][z] == True):
            #     answer += checkNumOfOutsideFreeSides(map, [x, y, z])
            #     answer2 += checkNumOfFreeSides(map, [x, y, z])
            #     print(answer)
            #     print(answer2)
                #
                #  print(x, y, z)
                # print(answer)
            #
            # else:
            #     if (seeIfAllAroundTrue(x, y, z) == True):
            #         answer -= 6
print(answer)

print(4482 - answer)
# 4454 is too low

# part 2 2445 ? nope ... too low
# part 2 2536 is too low
# part 2 2546 is too low
# part 2 4194 is just wrong

# part 1 answer was 4482
#######
# added = True
# counter = 0
# while (counter < size/2):
#     #added = False

#     upTo = size - counter - 1 - 1
#     for i in range(counter, upTo):
#         for j in range(counter, upTo):
#             if (checkIfOutSide([i, j, upTo])):
#                 map[i][j][upTo] = outside
#             if (checkIfOutSide([i, j, counter])):
#                 map[i][j][counter] = outside
#             if (checkIfOutSide([i, upTo, j])):
#                 map[i][upTo][j] = outside
#             if (checkIfOutSide([i, counter, j])):
#                 map[i][counter][j] = outside
#             if (checkIfOutSide([upTo, i, j])):
#                 map[upTo][i][j] = outside
#             if (checkIfOutSide([counter, i, j])):
#                 map[counter][i][j] = outside
#     counter += 1
#######
