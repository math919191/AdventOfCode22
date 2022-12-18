input = open("input.txt", "r")
map = []

for x in range(23):
    xMap = []
    for y in range(23):
        xMap.append([])
        for z in range(23):
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


answer = 0
for x in range(22):
    for y in range(22):
        for z in range(22):
            if (map[x][y][z]):
                answer += checkNumOfFreeSides(map, [x, y, z])

print(answer)

# 4454 is too low
