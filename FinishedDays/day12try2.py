from collections import deque

input = open("input.txt", "r")


class Vertex:
    def __init__(self):
        self.x = ''
        self.y = ''
        self.visited = False
        self.elevation = ""
        self.parent = ""


# init map and read input
elevationMap = []
vertexMap = []
start = ""
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
            start = v
        elif (v.elevation == -27):
            v.elevation = int(ord("z") - 96)  # setting E to height z
            end = v
        row.append(v)
        y += 1
    vertexMap.append(row)
    x += 1


def getNeighbors(vertex):
    x = vertex.x
    y = vertex.y

    neighbors = []
    if (x + 1 < len(vertexMap)):
        if (vertexMap[x][y].elevation - vertexMap[x+1][y].elevation >= -1):
            neighbors.append(vertexMap[x+1][y])
    if (y + 1 < len(vertexMap[0])):
        if (vertexMap[x][y].elevation - vertexMap[x][y+1].elevation >= -1):
            neighbors.append(vertexMap[x][y+1])
    if (x - 1 >= 0):
        if (vertexMap[x][y].elevation - vertexMap[x-1][y].elevation >= -1):
            neighbors.append(vertexMap[x-1][y])
    if (y - 1 >= 0):
        if (vertexMap[x][y].elevation - vertexMap[x][y-1].elevation >= -1):
            neighbors.append(vertexMap[x][y-1])
    return neighbors


# have a marked Bool map -- this is in the vertex class

# make a queue
queue = deque()

# mark start as visited
#start.visited = True
# add the start vertex to the queue
queue.append(start)

# while the queue isn't empty
while (len(queue) > 0):
    # pop off the first item in the queue
    item = queue.popleft()
    # if that item hasn't been visited
    if (item.visited == False):
        # visit that item
        item.visited = True
        neighbors = getNeighbors(item)

        # go through each neighbors
        for neighbor in neighbors:
            # if the neighbor hasn't been visited
            if (neighbor.visited) != True:
                # then append the neighbor to the queue
                queue.append(neighbor)
                # make the neighbor parent the current node we are working with
                neighbor.parent = item
                # check if that neighbor is our destination
                if (neighbor.x == end.x and neighbor.y == end.y):
                    # if it is...then return
                    print("made it....")
# now figure out how long the path actually is


parent = end
path = []
while (parent != start):
    #print(parent.x, parent.y)
    path.append([parent.y, parent.x])
    parent = parent.parent
path.reverse()
print(len(path))
