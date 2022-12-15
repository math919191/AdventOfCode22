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
            #opens = i
        elif ((line[i] == ',' and parenCounter == 1) or (i == (len(line)-1))):
            element = line[opens+1:i]  # .split(",")
            elements.append([])
            elements[commaCounter] = element
            commaCounter += 1
            opens = i

        elif line[i] == ']':
            parenCounter -= 1

    return elements


def comp(element1, element2):
    if (len(element1) == 0 or len(element2) == 0):
        if (len(element1) == 0):
            #print("TRUE: out of items on the left")
            return True
        if (len(element2) == 0):
            #print("FALSE: out of items on the right")
            return False

    if (element1[0] != "[" and element2[0] != "["):
        if (int(element1[0]) < int(element2[0])):
            #print("TRUE:", element1, element2)
            return True
        elif (int(element1[0]) > int(element2[0])):
            #print("FALSE:", element1, element2)
            return False
        elif (int(element1[0]) == int(element2[0])):
            # print("same")
            return

    if (element1[0] == "["):
        element1 = splitIntoElements(element1)
    if (element2[0] == "["):
        element2 = splitIntoElements(element2)

    for i in range(len(element1)):
        if (len(element2) <= i):
            #print("FALSE: out of range right!")
            return False
        comp(element1[i], element2[i])
    if (len(element1) < len(element2)):
        #print("TRUE: ran out of left!")
        return True


# test1 = splitIntoElements("[1,1,3,1,1]")
# test2 = splitIntoElements("[1,1,5,1,1]")
for i in range(len(pairs)):
    print(i+1, ": ", end="")
    print(comp(pairs[i][0], pairs[i][1]))
    print("")
