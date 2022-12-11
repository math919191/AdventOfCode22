from sys import stdin, stdout
p = []
for i in stdin:
    p.append(i.strip())

for i in range(len(p)):
    if (i != 0 and i % 2 == 1):
        print(p[i])
        q = p[i].split(" ")
        for j in range(len(q)):
            q[j] = int(q[j])
        q.sort()
        yes = (q[-1] - q[0]) * 2
        print(yes)


# for i in range(len(p)):
#     p[i] = p[i].lower()

# if (len(set(p)) == len(p)):
#     print("yes")
# else:
#     print("no")


# from sys import stdin, stdout
# p = []
# for i in stdin:
#     p = i.split(" ")

# answer = 1
# for i in p:
#     answer = answer * int(i)
# print(answer)
