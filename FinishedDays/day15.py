input = open("input.txt", "r")


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


def findWhereCantBe(sensorX, sensorY, beaconX, beaconY, coorOnLine, lineNum):
    distFromSensor = abs(lineNum - sensorY)
    # sensorRange = sensorX +- ( ( xDiff+yDiff ) - distFromSensor)
    xDiff = abs(sensorX - beaconX)
    yDiff = abs(sensorY - beaconY)

    for i in range((xDiff + yDiff) - distFromSensor + 1):
        coorOnLine.add(sensorX + i)
        coorOnLine.add(sensorX - i)


lines = readInput(input)
coorOnLine = set()
beaconsOnLine = set()
lineNum = 2000000

for coors in lines:
    findWhereCantBe(coors[0], coors[1], coors[2],
                    coors[3], coorOnLine, lineNum)
    if (coors[3] == lineNum):
        beaconsOnLine.add((coors[2], coors[3]))

# 6030937 is too high --- don't use the example line number
print(len(coorOnLine) - len(beaconsOnLine))
