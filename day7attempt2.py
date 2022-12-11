from sys import stdin, stdout
lines = []

for line in stdin:
    lines.append(line.strip())

### copied from stack overflow and then heavily modified ###


class Tree(object):
    "Generic tree node."

    def __init__(self, name='root', parent='parent', size=0, children=None):
        self.name = name
        self.size = size
        self.children = []
        self.parent = parent
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def add_child(self, node):
        #assert isinstance(node, Tree)
        self.children.append(node)

    def set_children(self, newChildren):
        self.children = newChildren

    def edit_children(self, dirToChange, newChildren):

        for i in range(len(self.children)):
            if (str(self.children[i].__repr__()) == str(dirToChange)):
                # print(self.children[i].get_children())
                self.children[i].set_children(newChildren)
                # print(self.children[i].get_children())
                return self.children[i]

    def get_child(self, dirName):
        for i in range(len(self.children)):
            if (str(self.children[i].__repr__()) == str(dirName)):
                return self.children[i]


root = Tree("root", None, 0, [])
slashTree = Tree("/", root, 0, [])
root.add_child(slashTree)
currLine = 0


def addDirAndChildren(dirName, currLineNum, parentTree, input):
    # print(parentTree)
    #print("parent: ", parentTree.__repr__())
    #print("child: ", dirName)
    # the line that we are currently on with dir name
    if (currLineNum == (len(input))):
        print("DONE")
        return

    #myLine = input[currLine].split(" ")
    if (dirName != ".."):
        dirNameTree = parentTree.get_child(dirName)

        currDirChildren = []  # init

        currLineNum += 2  # jump over the ls

        while (currLineNum < (len(input)) and input[currLineNum].split(" ")[0] != "$"):
            sizeOrDir, name = input[currLineNum].split(" ")
            currDirChildren.append(Tree(name, dirNameTree, sizeOrDir, None))
            currLineNum += 1

        childTree = parentTree.edit_children(dirName, currDirChildren)

        if (int(currLineNum) == int(len(input))):
            print("DONE")
            return

        addDirAndChildren(input[currLineNum].split(
            " ")[2], currLineNum, childTree, input)
    elif (dirName == ".."):
        #        print("going back")
        addDirAndChildren(input[currLineNum+1].split(" ")
                          [2], currLineNum+1, parentTree.get_parent(), input)


def printTree(tree, indent):
    for child in tree.get_children():
        if child.size == "dir":
            print(indent, "-", child.__repr__())
            printTree(child, indent + "  ")
        else:
            print(indent, "-", child.__repr__(), "(", child.size, ")")


def sumSizes(tree, total):
    for child in tree.get_children():
        if child.size == "dir":
            sumSizes(child, total)
        else:
            total.append(int(child.size))
    myTotal = 0
    for i in total:
        myTotal += i
    return myTotal


addDirAndChildren("/", 0, root, lines)
#printTree(slashTree, " ")

#print("myTotal", sumSizes(slashTree, []))


def GetTreeSums(tree, sums):
    for child in tree.get_children():
        if child.size == "dir":
            sums.append(sumSizes(child, []))
            GetTreeSums(child, sums)
    return sums


finalSum = 0
for sum in GetTreeSums(slashTree, []):
    if (sum < 100000):
        finalSum += sum
        # print(sum)

# 70000000
# 30000000
# 1644735
print(finalSum)
# 70000000 - total space

#print("myTotal", sumSizes(slashTree, []))

totalSum = sumSizes(slashTree, [])
dirSums = GetTreeSums(slashTree, [])

neededSpace = totalSum - 40000000

minAmount = totalSum
for i in dirSums:
    if (i > (neededSpace) and i < minAmount):
        minAmount = i

print(minAmount)
