from sys import stdin, stdout

lines = []
total = 0
for line in stdin:
    line = line.strip()
    # lines.append(line.strip())
    # print(line)

    if ((len(line.split(" "))) == 2):
        a, b = line.split(" ")

        if (int(b) < 100000):
            print(int(b))
            total += int(b)
print(total)
