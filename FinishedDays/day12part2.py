from collections import deque
import copy

input = open("input.txt", "r")


class Vertex:
    def __init__(self):
        self.x = ''
        self.y = ''
        self.visited = False
        self.elevation = ""
        self.parent = ""


def getNeighbors(vertex, vMap):
    x = vertex.x
    y = vertex.y

    neighbors = []
    if (x + 1 < len(vMap)):
        if (vMap[x][y].elevation - vMap[x+1][y].elevation >= -1):
            neighbors.append(vMap[x+1][y])
    if (y + 1 < len(vMap[0])):
        if (vMap[x][y].elevation - vMap[x][y+1].elevation >= -1):
            neighbors.append(vMap[x][y+1])
    if (x - 1 >= 0):
        if (vMap[x][y].elevation - vMap[x-1][y].elevation >= -1):
            neighbors.append(vMap[x-1][y])
    if (y - 1 >= 0):
        if (vMap[x][y].elevation - vMap[x][y-1].elevation >= -1):
            neighbors.append(vMap[x][y-1])
    return neighbors


def BFS(start, end, vertexMap):
    gotToEnd = False
    # make a queue
    queue = deque()
    # add the start vertex to the queue
    queue.append(start)

    start.visited = True
    # while the queue isn't empty
    while (len(queue) > 0):
        # pop off the first item in the queue
        node = queue.popleft()
        # if that item hasn't been visited
        # visit that item
        neighbors = getNeighbors(node, vertexMap)

        # go through each neighbors
        for neighbor in neighbors:
            # if the neighbor hasn't been visited
            if (neighbor.visited != True):
                # then append the neighbor to the queue
                queue.append(neighbor)
                neighbor.visited = True
                # make the neighbor parent the current node we are working with
                neighbor.parent = node
                # check if that neighbor is our destination
                if (neighbor == end):
                    # if it is...then return
                    print("made it....")
                    gotToEnd = True
                    # now figure out how long the path actually is
    if (gotToEnd):
        parent = end
        path = []
        while (parent != start):
            path.append([parent.x, parent.y])
            parent = parent.parent
        path.reverse()
        return len(path)
    else:
        return 91919191


# init map and read input
elevationMap = []
origVertexMap = []

possibleStarts = []
end = ""
x = 0

for line in input:
    heights = [int(ord(x) - 96) for x in line.strip()]
    elevationMap.append(heights)

    row = []
    y = 0
    for c in line.strip():
        v = Vertex()
        v.x = x
        v.y = y
        v.elevation = int(ord(c) - 96)
        if (v.elevation == -13):
            v.elevation = 1  # setting S to height a
        elif (v.elevation == -27):
            v.elevation = int(ord("z") - 96)  # setting E to height z
            end = v
        row.append(v)
        y += 1
        if (v.elevation == 1):
            possibleStarts.append(v)
    origVertexMap.append(row)
    x += 1

minPath = 1000000
for s in possibleStarts:
    vMap = copy.deepcopy(origVertexMap)
    pathLen = BFS(vMap[s.x][s.y], vMap[end.x][end.y], vMap)
    #print("start", s.x, s.y)
    # print(pathLen)
    minPath = min(minPath, pathLen)

print(minPath)
