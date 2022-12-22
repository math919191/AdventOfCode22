from collections import deque
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


def getMaxGeos(robot):

    for i in range(24):

        possibleMachines = getPossibleMachinesToIncrement(robot)

        incrementMaterials(robot)

        if (len(possibleMachines) > 0):
            robot = incrementMachine(possibleMachines[0], robot)

        # options now exist:
        # build a clay bot?
        # build a ore bot?
        # build a obs bot?
        # build a geo bot?
    return robot["geo"]


print(getMaxGeos(robot))
print("test")
