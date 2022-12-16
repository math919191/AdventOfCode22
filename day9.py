f = open("input.txt", "r")

directions = []
for line in f:
    a, b = line.split(" ")
    directions.append([a, int(b)])

visited = []
t = [0, 0]
h = [0, 0]
oldH = h


def checkAdj(t, h):
    if (abs(t[0]-h[0]) <= 1 and abs(t[1]-h[1]) <= 1):
        return True
    else:
        return False


for d in directions:
    for i in range(d[1]):
        oldH = [h[0], h[1]]
        if (d[0] == "R"):
            h[0] = h[0] + 1
        elif (d[0] == "L"):
            h[0] = h[0] - 1
        elif (d[0] == "D"):
            h[1] = h[1] - 1
        elif (d[0] == "U"):
            h[1] = h[1] + 1
        print(h)
        if (checkAdj(t, h) == False):
            stringifyT = str(t[0]) + "," + str(t[1])
            # print(stringifyT)
            if (stringifyT == "3,2"):
                print("here")
            visited.append(stringifyT)
            t = oldH
            #stringifyT = str(t[0]) + "," + str(t[1])
            # print(stringifyT)


print(visited)
mySet = set(visited)
print(len(visited), len(mySet)+1)

# 9040 too high
# 6493 too low
# needed to add one
