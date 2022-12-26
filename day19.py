from collections import deque
import copy
# Blueprint 1:  Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
input = open("input.txt", "r")
robots = []
for line in input:
    robot = dict()
    split = line.strip().split(" ")
    robot["oreBotCost"] = int(split[7])
    robot["clayBotCost"] = int(split[13])
    robot["obsBotCostOre"] = int(split[19])
    robot["obsBotCostClay"] = int(split[22])
    robot["geoBotCostOre"] = int(split[28])
    robot["geoBotCostObs"] = int(split[31])
    robot["clay"] = 0
    robot["ore"] = 0
    robot["obs"] = 0
    robot["geo"] = 0
    robot["clayBots"] = 0
    robot["oreBots"] = 1
    robot["obsBots"] = 0
    robot["geoBots"] = 0
    robot["prevAdded"] = []

    robots.append(robot)


def incrementMaterials(robot):
    # increment each material so we can see how many we have
    for material in ("clay", "ore", "obs", "geo"):
        botName = material + "Bots"
        numBots = robot[botName]
        robot[material] += numBots


def getPossibleMachinesToIncrement(robot):
    combos = []
    # ore       robots cost Ore
    oreBots = robot["ore"] // robot["oreBotCost"]
    # clay      robots cost Ore
    clayBots = robot["ore"] // robot["clayBotCost"]
    # obsidian  robost cost ore and clay
    obsBots = min([robot["ore"] // robot["obsBotCostOre"],
                  robot["clay"] // robot["obsBotCostClay"]])
    # geode     robots cost ore and obsidian
    geoBots = min([robot["ore"] // robot["geoBotCostOre"],
                  robot["obs"] // robot["geoBotCostObs"]])

    if (geoBots > 0):
        combos.append("geo")
    if (obsBots > 0):
        combos.append("obs")
    if (clayBots > 0):
        combos.append("clay")
    if (oreBots > 0):
        combos.append("ore")

    combos.append("none")
    return combos


def incrementMachine(machineName, robot):
    if (machineName == "clay"):
        robot["clayBots"] += 1
        robot["ore"] = robot["ore"] - robot["clayBotCost"]
    elif (machineName == "ore"):
        robot["oreBots"] += 1
        robot["ore"] = robot["ore"] - robot["oreBotCost"]
    elif (machineName == "obs"):
        # obsidian  robost cost ore and clay
        robot["obsBots"] += 1
        robot["ore"] = robot["ore"] - robot["obsBotCostOre"]
        robot["clay"] = robot["clay"] - robot["obsBotCostClay"]
    elif (machineName == "geo"):
        # geode     robots cost ore and obsidian
        robot["geoBots"] += 1
        robot["ore"] = robot["ore"] - robot["geoBotCostOre"]
        robot["obs"] = robot["obs"] - robot["geoBotCostObs"]

    return robot


def getMaxGeoCountFromQueue(q):
    maxGeo = 0
    for r in q:
        maxGeo = max(r["geo"], maxGeo)
    return maxGeo


def getMaxObsCountFromQueue(q):
    maxObs = 0
    for r in q:
        maxObs = max(r["obs"], maxObs)
    return maxObs


def getMaxesForInput():
    maxes = dict()
    return maxes


def shouldBuild(bot, possibleMachines, maxGeo):
    newRobots = []
    # Always build a geode robot if you can
    if (possibleMachines[0] == "geo"):
        newBot = incrementMachine("geo", bot)
        newRobots.append(newBot)
        return newRobots

    # Then always build a obsidian robot if you can
    if (possibleMachines[0] == "obs"):
        newBot = incrementMachine("obs", bot)
        newRobots.append(newBot)
        return newRobots

    # Ignore any state lagging behind the best geode bot count by 2 or more
    if (bot["geo"]+2 < maxGeo):
        return []

    # If you skipped building a robot on the turn before, don't just build it here for kicks

    # Ignore any state lagging behind the largest count of non-ore bots by 10 or more
    # (this is probably not guaranteed to give an optimal solution but does work for my inputs
    # and cuts the search space down a chunk).

    # Calculate the max theoretical geode possible at a given state.
    # If it's lower than the max score seen so far, abort the branch.

    # Keep track of the max resource at each state where state = {time,robots}.
    # If a branch has the same {time,robots} but has less resources - prune it.

    # Don't build more robo for a certain resource type if the factory will not be
    # able to consume it in one go.

    for machine in possibleMachines:
        newBot = copy.deepcopy(bot)
        newBot = incrementMachine(machine, newBot)
        newRobots.append(newBot)

    return newRobots


def checkIfSeen(robot, checkDuplicates):
    a = robot["clay"]
    b = robot["ore"]
    c = robot["obs"]
    d = robot["geo"]
    e = robot["clayBots"]
    f = robot["oreBots"]
    g = robot["obsBots"]
    h = robot["geoBots"]
    myStrRep = str(a) + " " + str(b) + " " + str(c) + " " + str(d) + \
        " " + str(e) + " " + str(f) + " " + str(g) + " " + str(h)
    if myStrRep in checkDuplicates:
        return True
    else:
        checkDuplicates.add(myStrRep)
        return False


def getMaxGeosBFS(robot):
    checkDuplicates = set()
    q = deque()
    q.append(robot)
    maxGeo = 0
    for i in range(24):
        newQ = deque()
        # Use a hash set for speed and to make sure states are unique
        # (not sure if two paths can lead to the same state but my gut feeling is they can)

        while (len(q) > 0):
            currBot = q.popleft()

            possibleMachines = getPossibleMachinesToIncrement(currBot)

            incrementMaterials(currBot)

            maxGeo = max(currBot["geo"], maxGeo)

            possibleBranches = shouldBuild(currBot, possibleMachines, maxGeo)

            for branch in possibleBranches:
                if (checkIfSeen(branch, checkDuplicates) == False):
                    newQ.append(branch)

        #print(str(i) + ":" + str(len(newQ)))
        q = copy.deepcopy(newQ)
        # options now exist:
        # build a clay bot?
        # build a ore bot?
        # build a obs bot?
        # build a geo bot?
    return getMaxGeoCountFromQueue(q)


qualityLevels = 0

counter = 1
for r in robots:
    maxGeo = getMaxGeosBFS(r)
    qualityLevel = counter * maxGeo
    print(qualityLevel)
    qualityLevels += qualityLevel
    counter += 1
print("answer 1: ", qualityLevels)
