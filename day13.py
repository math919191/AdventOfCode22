import sys
original = sys.stdout
sys.stdout = open('output.txt', 'w')
print('this is your redirected text:')


f = open("input.txt", "r")

pairs = []

currPair = []
for line in f:
    if (line == '\n'):
        pairs.append(currPair)
        currPair = []
    else:
        currPair.append(line.strip())


def splitIntoElements(line):
    parenCounter = 0
    commaCounter = 0
    opens = 0

    elements = []
    for i in range(len(line)):
        if (line[i] == '['):
            parenCounter += 1
            # opens = i
        elif ((line[i] == ',' and parenCounter == 1) or (i == (len(line)-1))):
            element = line[opens+1:i]  # .split(",")
            elements.append([])
            elements[commaCounter] = element
            commaCounter += 1
            opens = i

        elif line[i] == ']':
            parenCounter -= 1

    if (len(line) == 3 or len(line) == 4) and line[0] == "[" and line[-1] == "]":
        return [line[1:-1]]

    return elements


realOutput = True


def ranOutOnRight(element2):
    if (len(element2) == 0 or element2[0] == ""):
        return True
    else:
        return False


def ranOutOnLeft(element1):
    if (len(element1) == 0 or element1[0] == ""):
        return True
    else:
        return False


def canCompare(element1, element2):
    # if element1[0] != "[" and element2[0] != "[":
    #     return True
    split1 = splitIntoElements(element1)
    split2 = splitIntoElements(element2)
    if len(split1) == 1 and len(split2) == 1:
        return True
    return False


def convertToIntsIfNecessary(el1, el2):
    if el1[0] == "[" and len(el1) == 1:
        el1 = el1[1:-1]
    if el2[0] == "[" and len(el2) == 1:
        el2 = el2[1:-1]
    return el1, el2


def convertIfNecessary(element1, element2):
    if element1[0] == "[":
        element1 = splitIntoElements(element1)
    if element2[0] == "[":
        element2 = splitIntoElements(element2)
    return element1, element2


def comp(element1, element2):
    if (ranOutOnLeft(element1)):
        print("TRUE: out of items on the left")
        return True
    if (ranOutOnRight(element2)):
        print("FALSE: out of items on the right")
        return False

    if (canCompare(element1, element2)):
        element1[0], element2[0] = convertIfNecessary(element1[0], element2[0])
        element1[0], element2[0] = convertToIntsIfNecessary(
            element1[0], element2[0])
        if (int(element1[0]) < int(element2[0])):
            print("TRUE:", element1, element2)
            return True
        elif (int(element1[0]) > int(element2[0])):
            print("FALSE:", element1, element2)
            return False
        elif (int(element1[0]) == int(element2[0])):
            print("same")
            element1.pop(0)
            element2.pop(0)

    else:
        element1, element2 = convertIfNecessary(element1, element2)
        # splitting both element 1 and element 2 into individual numbers

    return comp(element1, element2)
    # for i in range(len(element1)):
    #     if (len(element2) <= i):
    #         if (firstTime):
    #             print("FALSE: out of range right!")
    #             firstTime = False
    #         return False
    #     comp(element1[i], element2[i], firstTime)
    # if (len(element1) < len(element2)):
    #     if (firstTime):
    #         print("TRUE: ran out of left!")
    #         firstTime = False
    #         return True
    # #print("got to the end?")


# test1 = splitIntoElements("[1,1,3,1,1]")
# test2 = splitIntoElements("[1,1,5,1,1]")
answer = 0
for i, pair in enumerate(pairs):
    valid = comp(pair[0], pair[1])
    if valid:
        answer += i
    print(i + 1, ": ", valid)

print(answer)
# sys.stdout = original
# f = open("output.txt", "r")
# count = 1
# answer = 0
# for line in f:
#     if (line.split(" ")[0] == str(count)):

#         if (line.split(" ")[2] == "TRUE:"):
#             answer += count
#             print(count)
#         count += 1

# print(answer)
# 5446 is too low

# 5506 is apparently the right answer
