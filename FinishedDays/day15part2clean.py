# From AoC reddit
# Part 2: same strategy as many people here,
# walk along the edge of the diamonds created by the sensors
# and for every of these positions,
# check if it is within range of any of the sensors.
# If not, we have found the result.

# create a sensor class
# contains sensor
# contains beacon
# contains function to check valid ranges
# contains function to walk on edge
global maxCoor
maxCoor = 4000000


class Sensor:
    def __init__(self, sx, sy, bx, by):
        self.sx = sx
        self.sy = sy
        self.bx = bx
        self.by = by
        self.diffX = abs(bx - sx)
        self.diffY = abs(by - sy)
        self.diff = abs(bx - sx) + abs(by - sy)

        self.minYInRange = sy - self.diffY
        self.maxYInRange = sy + self.diffY

        self.minXInRange = sx - self.diffX
        self.maxXInRange = sx + self.diffX

    def checksIfOutOfRange(self, givenX, givenY):

        distFromY = abs(givenY - self.sy)
        distFromX = abs(givenX - self.sx)

        if givenX < 0 or givenY < 0 or givenX > maxCoor or givenY > maxCoor:
            return False

        if self.diff < (distFromX + distFromY):
            return True
        else:
            return False

    def giveEdgePoints(self):
        edgePoints = []
        for i in range(self.diff + 1):
            x = self.sx
            y = self.sy

            # for j in ([0, 1], [0, -1], [1, 0], [-1, 0]):

            edgePoints.append(
                [x - self.diff + 1 + i, y + i])
            edgePoints.append(
                [x + self.diff + 1 - i, y + i])
            edgePoints.append(
                [x - self.diff + 1 + i, y - i])
            edgePoints.append(
                [x + self.diff + 1 - i, y - i])

        return edgePoints


# read input
def readInput():
    input = open("input.txt", "r")
    sensors = []
    for line in input:
        split = line.strip().split()
        sensorX = int(split[2].split("=")[1][:-1])
        sensorY = int(split[3].split("=")[1][:-1])
        beaconX = int(split[8].split("=")[1][:-1])
        beaconY = int(split[9].split("=")[1][:])
        sensors.append(Sensor(sensorX, sensorY, beaconX, beaconY))
    return sensors


sensors = readInput()


def findAnswer():
    for currSensor in sensors:

        edges = currSensor.giveEdgePoints()
        for edge in edges:
            if (edge[0] == 14 and edge[1] == 11):
                print("stop! wait a minute")
            overlapping = False
            overlappingSensors = 0

            for checkSensor in sensors:

                if (checkSensor.checksIfOutOfRange(edge[0], edge[1]) == False):
                    overlapping = True
                    overlappingSensors += 1
                    break
                else:
                    continue

            if overlapping == False:
                print("answer: ", edge)
                print("answer: ", edge[0]*4000000 + edge[1])
                return

            #print("overlapping sensors", overlappingSensors)
            overlapping = False


findAnswer()
# walk on the outside of diamond
# for each position
# see if it overlaps with any other sensors
# if it doesn't overlap, then we have found our answer
