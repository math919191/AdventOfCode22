f = open("input.txt", "r")
# init map and read input


class Vertex:
    def __init__(self):
        self.x = ''
        self.y = ''


elevation = []
neighbors = []

for line in f:
    heights = [int(ord(x) - 96) for x in line.strip()]
    elevation.append(heights)

    adjSingle = [[] for x in line.strip()]
    neighbors.append(adjSingle)

# create an adjacency List
for i in range(len(elevation)):
    for j in range(len(elevation[0])):
        currElevation = elevation[i][j]
        validNeighbors = []

#        if (elevation[i][j])
