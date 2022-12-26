
input = open("input.txt", "r")


# Part 2: same strategy as many people here,
# walk along the edge of the diamonds created by the sensors
# and for every of these positions,
# check if it is within range of any of the sensors.
# If not, we have found the result.


def readInput(input):
    lines = []
    for line in input:
        split = line.strip().split()
        sensorX = int(split[2].split("=")[1][:-1])
        sensorY = int(split[3].split("=")[1][:-1])
        beaconX = int(split[8].split("=")[1][:-1])
        beaconY = int(split[9].split("=")[1][:])
        lines.append([sensorX, sensorY, beaconX, beaconY])
    return lines


def findWhereCantBe(sensorX, sensorY, beaconX, beaconY, coorOnLine, lineNum, maxCoorNum):
    distFromSensor = abs(lineNum - sensorY)
    # sensorRange = sensorX +- ( ( xDiff+yDiff ) - distFromSensor)
    xDiff = abs(sensorX - beaconX)
    yDiff = abs(sensorY - beaconY)

    for i in range((xDiff + yDiff) - distFromSensor + 1):
        if (sensorX+i <= maxCoorNum):
            coorOnLine.add(sensorX + i)
        if (sensorX-i >= 0):
            coorOnLine.add(sensorX - i)


def getWhereCantBeForOneLine(lineNum, maxCoorNum):
    coorOnLine = set()
    beaconsOnLine = set()
    for coors in lines:
        findWhereCantBe(coors[0], coors[1], coors[2],
                        coors[3], coorOnLine, lineNum, maxCoorNum)
        if (coors[3] == lineNum):
            beaconsOnLine.add((coors[2], coors[3]))
            coorOnLine.add(coors[2])
    return coorOnLine


def findCoors(givenSet):
    i = 0
    while (True):
        if i in givenSet:
            i += 1
            continue
        else:
            break
    return i


lines = readInput(input)
maxCoorNum = 4000000
counter = 0
while (True):
    lineSet = getWhereCantBeForOneLine(counter, maxCoorNum)
    if (len(lineSet) == maxCoorNum+1):
        pass
    else:
        y = counter
        x = findCoors(lineSet)
        print("Answer", x, y)
        print(4000000*x + y)
        break
    counter += 1


# 1573500000000 is too low
# Answer 393375 0
# 1573500000000
#print(len(coorOnLine) - len(beaconsOnLine))
