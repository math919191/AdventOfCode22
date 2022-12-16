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


realOutput = True


def comp(element1, element2, firstTime):
    if (len(element1) == 0 or len(element2) == 0):
        if (len(element1) == 0):
            if (firstTime):
                print("TRUE: out of items on the left")
                realOutput = True
                firstTime = False
            return True
        if (len(element2) == 0):
            #print("FALSE: out of items on the right")
            if (firstTime):
                print("FALSE: out of items on the right")
                firstTime = False
            return False

    if (element1[0] != "[" and element2[0] != "["):
        if (int(element1[0]) < int(element2[0])):
            if (firstTime):
                print("TRUE:", element1, element2)
                firstTime = False
            return True
        elif (int(element1[0]) > int(element2[0])):

            if (firstTime):
                print("FALSE:", element1, element2)
                firstTime = False
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
            if (firstTime):
                print("FALSE: out of range right!")
                firstTime = False
            return False
        comp(element1[i], element2[i], firstTime)
    if (len(element1) < len(element2)):
        if (firstTime):
            print("TRUE: ran out of left!")
            firstTime = False
            return True
    #print("got to the end?")


# test1 = splitIntoElements("[1,1,3,1,1]")
# test2 = splitIntoElements("[1,1,5,1,1]")
for i in range(len(pairs)):
    print(i+1, ": ", end="")
    comp(pairs[i][0], pairs[i][1], True)

sys.stdout = original


f = open("output.txt", "r")

count = 1
answer = 0
for line in f:
    if (line.split(" ")[0] == str(count)):

        if (line.split(" ")[2] == "TRUE:"):
            answer += count
            print(count)
        count += 1
print(answer)
# 5446 is too low
