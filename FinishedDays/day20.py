import copy


class Number:
    def __init__(self, value):
        self.value = value


key = 811589153
input = open("input.txt", "r")
originalL = [Number(int(x) * key) for x in input]

l = originalL.copy()

numItems = len(l)

newIndex = 0

print(len(l), len(set(l)))


def findIndex(n):
    for i in range(len(l)):
        if (n == l[i]):
            return i


def findZero():
    for i in range(len(l)):
        if (l[i].value == 0):
            return i


def printNumbers(myL):
    for l in myL:
        print(l.value, end=",")
    print("")


for x in range(10):
    for num in originalL:
        index = l.index(num)  # findIndex(num)
        newIndex = (index + num.value) % (numItems-1)
        l.insert(newIndex, l.pop(index))
    # print("")
    # print("After", x+1, " rounds of mixing")
    # printNumbers(l)
# get the answer
# zeroIndex = findIndex(0)
#zeroIndex = l.index(0)
zeroIndex = findZero()
num1 = l[(zeroIndex + 1000) % (numItems)].value
num2 = l[(zeroIndex + 2000) % (numItems)].value
num3 = l[(zeroIndex + 3000) % (numItems)].value

print(num1 + num2 + num3)
#-6922 is wrong
