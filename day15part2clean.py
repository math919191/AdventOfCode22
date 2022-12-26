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

class Sensor:
    def __init__(self, sx, sy, bx, by):
        self.sx = sx
        self.sy = sy
        self.bx = bx
        self.by = by
        self.diffX = abs(bx - sx)
        self.diffY = abs(by - sy)

        self.minYInRange = sy - self.diffY
        self.maxYInRange = sy + self.diffY

        self.minXInRange = sx - self.diffX
        self.maxXInRange = sx + self.diffX

    def checksIfInRange(self, givenX, givenY):
        if (self.minYInRange < givenY < self.maxYInRange):
            if (abs(self.sx - givenX) <= self.diffX):
                return True
        else:
            return False
        return False

    def giveEdgePoints(self):
        edgePoints = []
        for i in range(self.diffY, ):
            x = self.sx
            y = self.sy

            for j in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                edgePoints.append([x + j[0], y + j[1]])

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
for currSensor in sensors:
    edges = currSensor.giveEdgePoints()
    for edge in edges:
        overlapping = False
        for checkSensor in sensors:
            if (checkSensor.checksIfInRange(edge[0], edge[1])):
                overlapping = True
                break
            else:
                continue

        if overlapping == False:
            print("answer: ", edge)
            break

# walk on the outside of diamond
    # for each position
        # see if it overlaps with any other sensors
        # if it doesn't overlap, then we have found our answer
