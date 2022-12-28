from collections import deque
import copy


class Valve:
    def __init__(self, name, flowRate, leadsTo):
        self.name = name
        self.flowRate = flowRate
        self.leadsTo = leadsTo


def readInput():
    input = open("input.txt", "r")
    valves = dict()
    for line in input:
        splitAtSemi = line.strip().split(";")
        part2 = splitAtSemi[1]

        parts = splitAtSemi[0].split(" ")
        name = parts[1]
        flowRate = int(parts[4].split("=")[1])

        part2 = part2.split(", ")
        leadsTo = []
        leadsTo.append(part2[0].split(" ")[-1])
        for i in range(1, len(part2)):
            leadsTo.append(part2[i])
        valve = Valve(name, flowRate, leadsTo)
        valves[name] = valve
    return valves


def validToExplore(curr, maxFlow, duplicates):
    if (curr[1] * 2 < maxFlow):
        return False
    else:
        return True


def getStrRep(curr):
    a = curr[0].name
    b = str(curr[1])
    c = ""

    for v in curr[2]:
        c = c + v

    strRep = a + " " + c + " " + b
    return strRep


def addToDuplicates(curr, duplicates):
    duplicates.add(getStrRep(curr))


def checkIfSeen(curr, duplicates):
    strRep = getStrRep(curr)
    if strRep in duplicates:
        return True
    else:
        duplicates.add(strRep)
        return False


def reduceDuplicates(q):
    itemsForNextRound = deque()
    existingItems = set()
    for item in q:
        strRep = getStrRep(item)
        if strRep in existingItems:
            pass
        else:
            existingItems.add(strRep)
            itemsForNextRound.append(item)
    l1 = len(existingItems)
    l2 = len(itemsForNextRound)
    return itemsForNextRound


def findMaxFlowRate(valves):
    maxFlow = 0

    q = deque()
    q.append([valves["AA"], 0, set()])

    for i in range(29, -1, -1):
        newQ = deque()
        duplicates = set()

        while len(q) > 0:
            curr = copy.deepcopy(q.popleft())
            possibleBranches = copy.deepcopy(curr[0].leadsTo)

            if (curr[0].name in curr[2]) == False and curr[0].flowRate > 0:
                possibleBranches.append("open")

            maxFlow = max(maxFlow, curr[1])

            for branch in possibleBranches:
                if branch == "open":
                    if curr[0].flowRate > 0:
                        curr[1] += (i * curr[0].flowRate)
                        curr[2].add(curr[0].name)
                        if (validToExplore(curr, maxFlow, duplicates)):
                            newQ.append([curr[0], curr[1], curr[2]])

                else:
                    if (validToExplore(curr, maxFlow, duplicates)):

                        newQ.append([valves[branch], curr[1], curr[2]])
        print("")
        print(i, len(newQ), maxFlow)
        newQ = reduceDuplicates(newQ)
        print(i, len(newQ), maxFlow)
        q = copy.deepcopy(newQ)
    print(maxFlow)
    return maxFlow


valves = readInput()
findMaxFlowRate(valves)

# 1829 is too high
# 1827 is too low

# turns out that I got the right answer! (:
# I was off by one on the example, so I tried adjusting the answer
# I got for that. But the answer it gave for my input was right!
# I am very pleased that I was able to finish at least part one for this.
# I did not copy any one else's code and BFS is starting to make a lot more sense for me
# I did read through some of the comments on reddit and copied parts of my code from day 19.
