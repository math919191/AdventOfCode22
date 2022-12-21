import operator
import copy


ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
}

input = open("input.txt", "r")

monkeyOps = dict()
hasVar = False

for line in input:
    split = line.strip().split(" ")

    settled = False
    if (len(split) == 2):
        settled = True
    monkeyOps[split[0][:-1]] = (split[1:], settled, hasVar)

# the dictionary is keeping track of 3 things
# 1 - the number or its own equation
# 2 - if it is settled
# 3 - if it has the variable from the equation in it
monkeyOps["humn"] = [["X"], True, True]


def checkIfInt(monkeyName):
    if (monkeyName == "humn" or monkeyName == ["X"]):
        return False
    value = monkeyOps[monkeyName][0]
    if (len(value) == 1):
        return True
    else:
        return False


def checkIfSettled(monkeyName):
    value = monkeyOps[monkeyName]
    if (value[1] == True):
        return True
    else:
        return False


def checkIfAllInts():
    if (monkey == "humn"):
        return False
    for monkey in monkeyOps:
        if (checkIfInt(monkey) == False):
            return False
    return True


def checkIfAllSettled():
    for monkey in monkeyOps:
        if (checkIfSettled(monkey) == False):
            return False
    return True


def part1():
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
    return monkeyOps["root"]


def hasVar(monkeyName):
    return monkeyOps[monkeyName][2]


def getEquationOrInt(monkeyName):
    currMonkey = monkeyOps[monkeyName]
    if (len(currMonkey[0]) > 1):
        return (currMonkey[0])
    if (checkIfInt(monkeyName)):
        return int(currMonkey[0][0])
    else:
        return (currMonkey[0])


while (checkIfAllSettled() != True):  # until we can still simplify, keep going
    for monkey, op in monkeyOps.items():  # loop through all the monkeys
        if (checkIfSettled(monkey) == False):  # see if it already done with

            monkey1 = op[0][0]
            monkey2 = op[0][2]
            # handle it a little different if it has a variable
            if (hasVar(monkey1) or hasVar(monkey2)):
                if (checkIfSettled(monkey1) and checkIfSettled(monkey2)):
                    newEquation = [getEquationOrInt(
                        monkey1), op[0][1], getEquationOrInt(monkey2)]
                    monkeyOps[monkey] = [newEquation, True, True]
            else:
                # handle the monkey the same way as we did the first time
                if (checkIfInt(monkey1) and checkIfInt(monkey2)):
                    #                   ops["+"](1,1)
                    num1 = int(monkeyOps[monkey1][0][0])
                    num2 = int(monkeyOps[monkey2][0][0])
                    newNum = ops[op[0][1]](num1, num2)
                    monkeyOps[monkey] = [[newNum], True, False]

print(monkeyOps["root"][0])
equation = "[[[[521, '+', [2, '*', [130833695252697, '-', [[[[[[[[[3, '*', [[[[4, '*', [[[[[[[[[[[[[[[[371, '+', [[[[[433, '+', [[[[[[120, '+', [[[[[[[[475, '+', [414, '+', [[[[[[[[[[[531, '+', [[378, '+', [[[[[700, '+', ['X']], '/', 3], '-', 913], '*', 77], '+', 673]], '+', 792]], '/', 2], '-', 178], '*', 2], '-', 69], '/', 5], '+', 363], '*', 2], '+', 559], '*', 3], '-', 748]]], '/', 6], '-', 808], '/', 7], '+', 175], '*', 53], '-', 851], '/', 3]], '*', 2], '+', 826], '/', 9], '-', 156], '*', 15]], '+', 511], '/', 2], '-', 704], '*', 2]], '*', 2], '-', 984], '/', 10], '+', 521], '/', 2], '-', 309], '*', 6], '-', 626], '*', 2], '+', 680], '/', 2], '-', 625], '+', 12], '/', 5], '+', 161]], '-', 895], '/', 3], '+', 315]], '+', 258], '/', 9], '-', 77], '*', 18], '-', 601], '*', 2], '+', 17], '/', 3]]]], '/', 3], '+', 31343426392931], True, True]"
equation = equation.replace("[", "(").replace("]", ")").replace(
    ",", "").replace("'", "")
# So... after I generated this equation, I just copied it into an online equation solver and it got me the answer below (:

print(equation)
print(1193432170233914368 / 393525)

# we want to go through the entire list until we have 2 things
# 1 - the first root number
# 2 - an equation to get the second root number
# and then we can just work out the answer by hand
# so we can do a while loop
#       if it is an equation with the var
#           We will replace its equation to allow it to grow
#       if is is not an equation with the var
#           Handle it the way we did the first time around
