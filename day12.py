# from sys import stdin, stdout
f = open("input.txt", "r")
# init map and read input
mymap = []
# stdin = input("get input")
for line in f:
    heights = [int(ord(x) - 96) for x in line.strip()]
    mymap.append(heights)
    print(heights)

# get the start and end coordinates
start = []
end = []
for i in range(len(mymap)):
    for j in range(len(mymap)):
        if (mymap[i][j] == -13):
            start = [i, j]
            mymap[i][j] = 1  # setting S to height a
        elif (mymap[i][j] == -27):
            end = [i, j]


def printMap(map):
    for x in map:
        for y in x:
            if (y == 'v' or y == '^' or y == '>' or y == '<'):
                print(y, end="")
            else:
                print(".", end="")
        print(" ")


def checkIfVisited(x, y, map):
    if (map[x][y] == "<" or map[x][y] == ">" or map[x][y] == "^" or map[x][y] == "v" or map[x][y] == "X"):
        return True
    else:
        return False


def canClimb(currX, currY, newX, newY, map):
    if (newX < 0 or newY < 0 or newX == len(map) or newY == len(map[0])):
        return False
    # if (map[newX][newY] == "X" or map[currX][currY] == "X"):
    #     return False
    if (checkIfVisited(newX, newY, map) or checkIfVisited(currX, currY, map)):
        return
    if ((map[newX][newY] - map[currX][currY]) <= 1):
        return True
    else:
        return False


def nextStep(x, y, numSteps, map):
    print(x, y)
    # reached S
    if (map[x][y] == -27):
        print(numSteps)
        printMap(map)

        map[x][y] = mymap[x][y]
        return
    if (map[x][y] == 6):
        print("EH")
    # base cases
    # out of bounds
    if (x < 0 or y < 0 or x == len(map) or y == len(map[0])):
        return
    # already visited
    # if (map[x][y] == "X"):
    #     return
    if (checkIfVisited(x, y, map)):
        return

    if (canClimb(x, y, x-1, y, map)):
        map[x][y] = "^"
        numSteps += 1
        nextStep(x-1, y, numSteps, map)
    if (canClimb(x, y, x+1, y, map)):
        map[x][y] = "v"
        numSteps += 1
        nextStep(x+1, y, numSteps, map)
    if (canClimb(x, y, x, y+1, map)):
        map[x][y] = ">"
        numSteps += 1
        nextStep(x, y+1, numSteps, map)
    if (canClimb(x, y, x, y-1, map)):
        map[x][y] = "<"
        numSteps += 1
        nextStep(x, y-1, numSteps, map)

    map[x][y] = mymap[x][y]
    # print(numSteps)
    return


print("hello world")
nextStep(0, 0, 0, mymap)
