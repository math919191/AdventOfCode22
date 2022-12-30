
# mostly copied code from my first try "day13.py"

def readInput():
    f = open("input.txt", "r")

    pairs = []

    currPair = []
    for line in f:
        if (line == '\n'):
            pairs.append(currPair)
            currPair = []
        else:
            currPair.append(line.strip())
    return pairs


def convertToListIfNecessary(el1, el2):
    if type(el1) is int:
        el1 = [el1]
    if type(el2) is int:
        el2 = [el2]
    return el1, el2


def comp(el1, el2):

    # check if there is a valid comparison
    if type(el1) is int and type(el2) is int:
        if (el1 < el2):
            return True
        elif el1 > el2:
            return False
        else:
            return "same"

    el1, el2 = convertToListIfNecessary(el1, el2)

    if len(el1) == 0 and len(el2) == 0:
        return "same"

    if len(el1) == 0:  # left side ran out
        return True
    if len(el2) == 0:  # right side ran out
        return False

    for i in range(len(el1)):
        if len(el1) > 0 and len(el2) == 0:
            return False
        pop1 = el1.pop(0)
        pop2 = el2.pop(0)
        compResult = comp(pop1, pop2)
        if (compResult == "same"):
            pass
        else:
            return compResult
    if len(el1) == 0 and len(el2) > 0:
        return True

    return "same"


pairs = readInput()
answer = 0
for i, pair in enumerate(pairs):
    e1 = eval(pair[0])
    e2 = eval(pair[1])
    # print(pair)
    if (i == 36):
        print("stop wait a minute")
    if comp(e1, e2):
        print(i+1)
        answer += (i + 1)

print(answer)
