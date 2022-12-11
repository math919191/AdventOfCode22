from sys import stdin, stdout
lines = []

for line in stdin:
    lines.append(line.strip())

### copied from stack overflow ###


class Tree(object):
    "Generic tree node."

    def __init__(self, name='root', parent='parent', size=0, children=None):
        self.name = name
        self.size = 0
        self.children = []
        self.parent = parent
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def get_parent(self):
        return self.parent

    def add_child(self, node):
        #assert isinstance(node, Tree)
        self.children.append(node)

    def set_children(self, newChildren):
        self.children = newChildren

    def edit_children(self, dirToChange, newChildren):

        for i in range(len(self.children)):
            print(str(self.children[i].__repr__()), str(dirToChange))
            if (str(self.children[i].__repr__()) == str(dirToChange)):
                # for child in newChildren:
                print(self.children[i].__repr__())
                self.children[i].set_children(newChildren)

                return self.children[i]

    def get_child(self, dirName):
        for i in range(len(self.children)):
            if (str(self.children[i].__repr__()) == str(dirName)):
                return self.children[i]


# def __init__(self, name='root', parent='parent', size=0, children=None):
root = Tree("root", None, 0, [])
slashTree = Tree("/", root, 0, [])
root.add_child(slashTree)
currLine = 0


def callThis():
    print("hello")


global DEATH
DEATH = False


def addDirAndChildren(dirName, currLineNum, parentTree, input):
    # the line that we are currently on with dir name
    dirNameTree = parentTree.get_child(dirName)
    if (currLineNum == (len(input))):
        print("DONE")
        return

    myLine = input[currLine].split(" ")
    # if (myLine[1] == "cd" and myLine[2] != ".."):
    if (dirName != ".."):
        currDirChildren = []  # init

        currLineNum += 2  # jump over the ls

        #sizeOrDir, name = input[currLineNum].split(" ")
        # keep going till we hit a cd command
        while (currLineNum < (len(input)) and input[currLineNum].split(" ")[0] != "$"):
            sizeOrDir, name = input[currLineNum].split(" ")
            currDirChildren.append(
                Tree(name, dirNameTree, sizeOrDir, None))
            print(input[currLineNum].split(" "))
            currLineNum += 1

        print("parentTreeName", parentTree.__repr__())
        childTree = parentTree.edit_children(
            dirName, currDirChildren)
        print("ChildTreeName", childTree.__repr__())

#        if (input[currLineNum].split(" ")[2] != ".."):
        if (int(currLineNum) == int(len(input))):
            print("DONE")
            return

        print(currLineNum, len(input))
        addDirAndChildren(input[currLineNum].split(
            " ")[2], currLineNum, childTree, input)
    elif (dirName == ".."):
        print("moving backwards")
        print(parentTree)
        addDirAndChildren(input[currLineNum+1].split(" ")
                          [2], currLineNum+1, parentTree.get_parent(), input)


addDirAndChildren("/", 0, root, lines)
