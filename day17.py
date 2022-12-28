
import copy


def readInput():
    input = open("input.txt", "r")
    lines = []
    for line in input:
        split = [x for x in line.strip()]

        return split


def findBottomLeftStartingCoor(chamber, rockNum):
    # Each rock appears so that its left edge is two units away from the left wall
    # and its bottom edge is three units above the highest rock in the room
    x = 2
    y = max(chamber) + 3

    if (rockNum == 1):  # rock 1 coordinate is tracked with it's left edge
        y += 1

    return [x, y]


def checkIfHitsRightWall(rockCoor, rockNum):
    if rockNum == 0:
        if rockCoor[0] == 3:
            return True
    elif rockNum == 1:
        if rockCoor[0] == 4:
            return True
    elif rockNum == 2:
        if rockCoor[0] == 4:
            return True
    elif rockNum == 3:
        if rockCoor[0] == 6:
            return True
    elif rockNum == 4:
        if rockCoor[0] == 5:
            return True

    return False


def checkIfHitsLeftRock(rockCoor, rockNum, chamber1):
    chamber = copy.deepcopy(chamber1)
    chamber = [x - 1 for x in chamber]
    if rockNum == 0:
        leftEdge = rockCoor[0]
        if chamber[leftEdge - 1] == rockCoor[1]:
            return True

    elif rockNum == 1:
        leftEdge = rockCoor[0]
        if chamber[leftEdge - 1] == rockCoor[1]:
            return True

        bottomLeftEdge = rockCoor[0] + 1
        if chamber[bottomLeftEdge + 1] == rockCoor[1]:
            return True

        topLeftEdge = rockCoor[0] + 1
        if chamber[bottomLeftEdge + 1] == rockCoor[1]:
            return True

    elif rockNum == 2:
        leftEdge = rockCoor[0]
        if chamber[leftEdge - 1] == rockCoor[1]:
            return True

    elif rockNum == 3:
        for i in range(4):
            leftEdge = rockCoor[0]
            if chamber[leftEdge - 1] == rockCoor[1] + i:
                return True

    elif rockNum == 4:
        for i in range(2):
            leftEdge = rockCoor[0]
            if chamber[leftEdge - 1] == rockCoor[1] + i:
                return True

    return False


def checkIfHitsRightRock(rockCoor, rockNum, chamber1):
    chamber = copy.deepcopy(chamber1)
    chamber = [x - 1 for x in chamber]
    if rockNum == 0:
        rightEdge = rockCoor[0] + 3
        if chamber[rightEdge + 1] == rockCoor[1]:
            return True

    elif rockNum == 1:
        rightEdge = rockCoor[0] + 2
        if chamber[rightEdge + 1] == rockCoor[1]:
            return True
        bottomRightEdge = rockCoor[0] + 1
        if chamber[bottomRightEdge + 1] == rockCoor[1] - 1:
            return True

    elif rockNum == 2:
        for i in range(3):
            rightEdge = rockCoor[0] + 2
            if chamber[rightEdge + 1] == rockCoor[1] + i:
                return True

    elif rockNum == 3:
        for i in range(4):
            rightEdge = rockCoor[0]
            if chamber[rightEdge + 1] == rockCoor[1] + i:
                return True

    elif rockNum == 4:
        for i in range(2):
            rightEdge = rockCoor[0] + 1
            if chamber[rightEdge + 1] >= rockCoor[1] + i:
                return True

    return False


def checkIfHitsLeftWall(rockCoor, rockNum):
    if rockCoor[0] == 0:
        return True
    else:
        return False


def moveRock(moveCounter, rockNum, movements, rockCoor):
    direction = movements[moveCounter % len(movements)]
    if (direction == ">"):
        # check if it'll hit the wall
        if (checkIfHitsRightWall(rockCoor, rockNum)):
            return rockCoor  # it doesn't change
        if (checkIfHitsRightRock(rockCoor, rockNum, chamber)):
            return rockCoor
        return [rockCoor[0] + 1, rockCoor[1]]
    elif (direction == "<"):
        # check if it'll hit the wall
        if (checkIfHitsLeftWall(rockCoor, rockNum)):
            return rockCoor  # it doesn't change
        if (checkIfHitsLeftRock(rockCoor, rockNum, chamber)):
            return rockCoor
        return [rockCoor[0] - 1, rockCoor[1]]
    print("error from move rock")


def fall(coor):
    coor = [coor[0], coor[1]-1]
    return coor


def checkIfHitBottom(chamber, rockCoor, rockNum):
    x = rockCoor[0]
    y = rockCoor[1] + 1
    if rockNum == 0:
        for i in range(4):
            if chamber[x + i] == y - 1:
                return True
    elif rockNum == 1:
        if chamber[x+1] == y - 1 - 1:
            return True
        if chamber[x] == y - 1:
            return True
        if chamber[x+2] == y - 1:
            return True
    elif rockNum == 2:
        for i in range(3):
            if chamber[x + i] == y - 1:
                return True
    elif rockNum == 3:
        if chamber[x] == y - 1:
            return True
    elif rockNum == 4:
        for i in range(2):
            if chamber[x + i] == y - 1:
                return True

    return False


def updateChamber(rockNum, chamber, rockCoor):
    x = rockCoor[0]
    y = rockCoor[1] + 1
    if rockNum == 0:
        for i in range(4):
            chamber[x + i] = y
    elif rockNum == 1:
        chamber[x+1] = y+1
        chamber[x] = y
        chamber[x+2] = y

    elif rockNum == 2:
        for i in range(2):
            chamber[x + i] = y
        chamber[x+2] = y + 2
    elif rockNum == 3:
        chamber[x] = y + 3
    elif rockNum == 4:
        for i in range(2):
            chamber[x + i] = y + 1

    return chamber


movements = readInput()
chamber = [0 for x in range(7)]

moveCounter = 0
for rockNum in range(2022):
    if (rockNum == 23):
        print("stop! Wait a minute")
    currRockNum = rockNum % 5

    rockCoor = findBottomLeftStartingCoor(chamber, currRockNum)

    hitRock = False

    while (hitRock == False):
        rockCoor = moveRock(moveCounter, currRockNum, movements, rockCoor)

        moveCounter += 1

        hitRock = checkIfHitBottom(chamber, rockCoor, currRockNum)

        if (hitRock == False):
            rockCoor = fall(rockCoor)

    chamber = updateChamber(currRockNum, chamber, rockCoor)
    print(rockNum, chamber)

print("part 1", max(chamber))
# The tall, vertical chamber is exactly seven units wide.
# (or the floor, if there isn't one).

# After a rock appears, it alternates between being pushed by a jet of hot gas
# one unit (in the direction indicated by the next symbol in the jet pattern)
# and then falling one unit down.
