import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
}
# print(ops["+"](1,1)) # prints 2


input = open("input.txt", "r")

monkeyOps = dict()

for line in input:
    split = line.strip().split(" ")

    monkeyOps[split[0][:-1]] = split[1:]


def checkIfInt(monkeyName):
    value = monkeyOps[monkeyName]
    if (len(value) == 1):
        return True
    else:
        return False


def checkIfAllInts():
    for monkey in monkeyOps:
        if (checkIfInt(monkey) == False):
            return False
    return True


while (checkIfAllInts() != True):
    for monkey, op in monkeyOps.items():
        if (checkIfInt(monkey) == False):  # see if it already is an int
            monkey1 = op[0]
            monkey2 = op[2]
            if (checkIfInt(monkey1) and checkIfInt(monkey2)):
                #                   ops["+"](1,1)
                num1 = int(monkeyOps[monkey1][0])
                num2 = int(monkeyOps[monkey2][0])

                newNum = ops[op[1]](num1, num2)
                monkeyOps[monkey] = [newNum]

print("Part 1:", monkeyOps["root"])
