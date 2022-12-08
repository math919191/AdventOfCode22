from sys import stdin, stdout
lines = []

for line in stdin:
    lines.append(line.strip())
lines.append("$ cd end")

root = []
currLevel = 0
currDirName = ""
currDir = []

directories = {}  # maps directory and all its dependencies
fileSizes = {}  # holds sizes of all files

#counter = 0
level = 0
for line in lines:
    lineSplit = line.split(" ")
    if (lineSplit[0] == "$"):

        if (lineSplit[1] == "cd" and lineSplit[2] != ".."):
            level += 1
            directories[currDirName] = (currDir)
            currDir = []
            currDirName = lineSplit[2]
            print(currDirName)

        else:
            level -= 1
        # elif (lineSplit[1] == "ls"):

    else:
        if (lineSplit[0] != "dir"):
            fileSizes[lineSplit[1]] = int(lineSplit[0])
        currDir.append([lineSplit[1], lineSplit[0]])

    counter += 1


dirSizes = {}
changes = True
while (changes):
    changes = False
    for key, value in directories.items():
        #tryToGetVal(key, value)
        total = 0
        successReturn = True
        for d in value:
            name = d[0]
            if name in fileSizes:  # it's settled
                total += int(fileSizes[name])
            else:
                changes = True
                successReturn = False
                break

        if successReturn:
            #changes = True
            # if (value == 'dir'):

            fileSizes[key] = int(total)
        #successReturn = True


answer = 0
dirBool = False
for a, b in fileSizes.items():
    print(a, b)
    if (b == 0):
        dirBool = True

    if (int(b) <= 100000 and dirBool):
        # print(b)
        answer += int(b)

print("answer: ", answer)

# 717595 is too low


# for key, value in directories.items():
#     print(key,  " : ", value)
# print(fileSizes)


# def tryToGetVal(dirname, dependencies):  # passing in just the dependencies
#     total = 0
#     for d in dependencies:
#         name = d[0]
#         if name in fileSizes:  # it's settled
#             total += fileSizes[name]
#         else:
#             return False

#     fileSizes[dirname] = total
#     return True
