from sys import stdin, stdout
lines = []

for line in stdin:
    lines.append(line.strip())

rows = []

register = 1
cycleneg1 = 0
cycleneg2 = 0

cycleNum = 0
signal = 0


def cycle(cycleNum, register, signal, rows):
    cycleNum += 1
    print(register, cycleNum)

    if (abs(int(cycleNum % 40) - 1 - int(register)) <= 1):
        rows.append("#")
    else:
        rows.append(".")
    return [cycleNum, register, signal, rows]


for line in lines:
    a = line.split(" ")
    if (a[0] == "addx"):
        cycleneg2 = int(a[1])

        cycleNum, register, signal, rows = cycle(
            cycleNum, register, signal, rows)
        cycleNum, register, signal, rows = cycle(
            cycleNum, register, signal, rows)

        register += cycleneg2

    else:
        cycleNum, register, signal, rows = cycle(
            cycleNum, register, signal, rows)

print(signal)

for i in range(len(rows)):
    print(rows[i], end="")
    if (i % 40 == 39):
        print("")
