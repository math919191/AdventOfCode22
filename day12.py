# from sys import stdin, stdout
f = open("input.txt", "r")
# init map and read input
mymap = []
visited = []
# stdin = input("get input")
for line in f:
    heights = [int(ord(x) - 96) for x in line.strip()]
    mymap.append(heights)

    visitedLine = [False for x in line.strip()]
    visited.append(visitedLine)
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


def checkIfVisited(x, y, visitedMap):
    if (visitedMap[x][y] == "<" or visitedMap[x][y] == ">" or visitedMap[x][y] == "^" or visitedMap[x][y] == "v" or visitedMap[x][y] == "X"):
        return True
    else:
        return False


def canClimb(currX, currY, newX, newY, map, visited):
    # check if

    if (newX < 0 or newY < 0 or newX == len(map) or newY == len(map[0])):
        return False

    if (checkIfVisited(newX, newY, visited)):  # or checkIfVisited(currX, currY, visited)
        return False

    if (map[currX][currY] == -27):
        # print()
        # printMap(map)
        map[currX][currY] = mymap[currX][currY]

    # if (canClimb(x, y, x-1, y, map)):

    # if (map[newX][newY] == "X" or map[currX][currY] == "X"):
    #     return False
    if ((map[newX][newY] - map[currX][currY]) <= 1):
        return True
    else:
        return False


steps = []


def nextStep(x, y, numSteps, map, visited):
    #print(x, y)
    # printMap(visited)
    #print(" ")
    # reached S
    if (map[x][y] == -27):
        print(numSteps)
        # printMap(visited)
        steps.append([numSteps, visited])
        return 0
    #     printMap(map)

    #     map[x][y] = mymap[x][y]
    #     return

    # base cases
    # out of bounds
    if (canClimb(x, y, x, y+1, map, visited)):
        visited[x][y] = ">"
        numSteps += 1
        nextStep(x, y+1, numSteps, map, visited)
    if (canClimb(x, y, x, y-1, map, visited)):
        visited[x][y] = "<"
        numSteps += 1
        nextStep(x, y-1, numSteps, map, visited)

    if (canClimb(x, y, x-1, y, map, visited)):
        visited[x][y] = "^"
        numSteps += 1
        nextStep(x-1, y, numSteps, map, visited)

    if (canClimb(x, y, x+1, y, map, visited)):
        visited[x][y] = "v"
        numSteps += 1
        nextStep(x+1, y, numSteps, map, visited)

    visited[x][y] = False
    #map[x][y] = mymap[x][y]
    numSteps -= 1
    # print(numSteps)
    return 0


print("hello world")
nextStep(0, 0, 0, mymap, visited)

currCount = steps[0][0]
currPath = []
for count in steps:
    if count[0] < currCount:
        currCount = count[0]
        currPath = count[1]

print("Answer: ", currCount)
print("curr path")
printMap(currPath)
