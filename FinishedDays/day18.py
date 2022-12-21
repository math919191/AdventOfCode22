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


def checkBounds(num):
    if (num >= 0 and num < (size)):
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


answer1 = 0
for x in range(size-1):
    for y in range(size-1):
        for z in range(size-1):
            if (map[x][y][z] == True):
                answer1 += checkNumOfFreeSides(map, [x, y, z])
print("Part 1:", answer1)

flood_fill(0, 0, 0)

insideSurface = 0
for x in range(size-1):
    for y in range(size-1):
        for z in range(size-1):
            if (map[x][y][z] == False):
                insideSurface += checkNumOfInsideSurface(map, [x, y, z])

print("Part 2:", answer1 - insideSurface)
# 4454 is too low

# part 2 2445 ? nope ... too low
# part 2 2536 is too low
# part 2 2546 is too low
# part 2 4194 is just wrong

# part 1 answer was 4482
