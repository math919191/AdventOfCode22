from sys import stdin, stdout
import math


def getNum(let):
    if ((let == 'A') or (let == 'X')):
        return 1
    elif (let == 'B' or (let == 'Y')):
        return 2
    elif (let == "X\n"):
        return 1
    elif (let == "Y\n"):
        return 2
    else:
        return 3


elf = ["A", "B", "C"]
# rock paper scissors
my = ["X", "Y", "Z"]

score = 0
for line in stdin:
    # print(line)
    # print(getNum(a), getNum(b))

    a, b = line.split(" ")

    if (getNum(b) == getNum(a)):
        # it's a tie
        # print("+3")
        score += 3
    elif (getNum(b) - getNum(a) == 1):  # scissors beats paper & paper beats rock (1) or s
        score += 6

    elif (getNum(b) - getNum(a) == -2):  # rock beats scissors
        # print("+6")
        score += 6
    # else:
        # print("+0")

    # print("+", getNum(b))
    score += getNum(b)
    # print("---\n")
print("Part 1: ", score)

# Part 1:  10947 is wrong
# 12249 is wrong
