from sys import stdin, stdout
import math


def getNum(let):
    if (let == 'A'):
        return 1
    elif (let == 'B'):
        return 2
    elif (let == 'C'):
        return 3


elf = ["A", "B", "C"]
# rock paper scissors
my = ["X", "Y", "Z"]

score = 0
for line in stdin:

    a, b = line.split(" ")

    if (b == "X\n"):  # lose
        score += 0
        if (a == "A"):
            score += 3
        elif (a == "B"):
            score += 1
        elif (a == "C"):
            score += 2
        # print("lose: ", score)

    elif (b == "Y\n"):  # tie
        score += 3
        score += getNum(a)
        # print("tie: ", score)
    elif (b == "Z\n"):  # win
        score += 6
        if (a == "A"):
            score += 2
        elif (a == "B"):
            score += 3
        elif (a == "C"):
            score += 1
        # print("win: ", score)
    else:
        print("ERROR")
        print(a, b)

print("Part 2: ", score)
