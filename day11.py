import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
}

input = open("input.txt", "r")
monkeys = []

# Parse Input
currMonkey = dict()
for line in input:
    splitLine = line.strip().split(" ")
    if (splitLine[0] == "Monkey"):
        if (splitLine[1] != '0:'):
            monkeys.append(currMonkey)
        currMonkey = dict()
        currMonkey["itemsInspected"] = 0
    elif (splitLine[0] == ''):
        continue
    elif (splitLine[0] == "Starting"):
        items = splitLine[2:]
        for i in range(len(items)-1):
            items[i] = int(items[i][:-1])
        items[-1] = int(items[-1])
        currMonkey["StartingItems"] = items
    elif (splitLine[0] == "Operation:"):
        operation = splitLine[3:]
        currMonkey["Operation"] = operation
    elif (splitLine[0] == "Test:"):
        currMonkey["Test"] = splitLine[1:]
    elif (splitLine[1] == "true:"):
        currMonkey["trueMonkey"] = int(splitLine[-1])
    elif (splitLine[1] == "false:"):
        currMonkey["falseMonkey"] = int(splitLine[-1])


def newWorryLevelFromOp(currWorry, operation):
    if (operation[2] == "old"):
        return (ops[operation[1]](currWorry, currWorry))
    else:
        return (ops[operation[1]](currWorry, int(operation[2])))


def printMonkeyItems(monkeys):
    counter = 0
    for monkey in monkeys:
        print("")
        print("Monkey", counter, ": ", end="")
        for item in monkey["StartingItems"]:
            print(item, end=",")
        counter += 1


def printMonkeyItemsInspected(monkeys):
    counter = 0
    for monkey in monkeys:
        print("")
        print("Monkey", counter, ": ", monkey["itemsInspected"], end="")
        counter += 1
    print("")


def getAnswerPart1(monkeys):
    numList = []
    for monkey in monkeys:
        numList.append(monkey["itemsInspected"])
    numList.sort(reverse=True)
    return numList[0] * numList[1]


def round(monkeys):
    for i in range(len(monkeys)):
        # loop thru all items
        monkeys[i]["itemsInspected"] += len(monkeys[i]["StartingItems"])
        for item in monkeys[i]["StartingItems"]:
            worryLevel = item
            # worry level is changed based on operation
            worryLevel = newWorryLevelFromOp(
                worryLevel, monkeys[i]["Operation"])
            # worry level is divied by 3 and rounded down
            worryLevel = worryLevel // 3
            # checks if worry level passes the test
            passes = (worryLevel % int(monkeys[i]["Test"][2]) == 0)
            if (passes):
                # throw the item to the true monkey
                trueMonkey = monkeys[i]["trueMonkey"]
                monkeys[trueMonkey]["StartingItems"].append(worryLevel)
            else:
                falseMonkey = monkeys[i]["falseMonkey"]
                monkeys[falseMonkey]["StartingItems"].append(worryLevel)

                # # throw the item to the false monkey
                # falseMonkey = monkeys[i]["falseMonkey"]
                # tryAgain = monkeys[falseMonkey]
                # #falseMonkeyItems = monkeys[falseMonkey]["StartingItems"]
                # falseMonkeyItems = falseMonkey["StartingItems"]
                # falseMonkeyItems.append(item)
                # monkeys[falseMonkey]["StartingItems"] = falseMonkeyItems
        monkeys[i]["StartingItems"] = []
    return monkeys


for i in range(20):
    # printMonkeyItems(monkeys)
    monkeys = round(monkeys)
printMonkeyItems(monkeys)
printMonkeyItemsInspected(monkeys)
print(getAnswerPart1(monkeys))
