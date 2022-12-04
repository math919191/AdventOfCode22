from sys import stdin, stdout

totals = []
for line in stdin:
    totals.append(line.strip())
# check for new line!

count = 0
for row in totals:
    c, d = row.split(",")
    c1, c2 = c.split('-')
    d1, d2 = d.split('-')
    d2 = d2.strip()
    if ((int(d1) >= int(c1)) and (int(d2) <= int(c2))):
        count += 1
    elif ((int(d1) <= int(c1)) and (int(d2) >= int(c2))):
        count += 1

print(count)
