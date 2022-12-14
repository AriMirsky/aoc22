from aocd import get_data, submit
import sys
import numpy as np

input = get_data(day=12, year=2022)
input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
lines = input.split("\n")

elevations = []

ans = 0
start = None
end = None
for y, line in enumerate(lines):
    elevations.append([])
    for x, char in enumerate(line):
        if char != "S" and char != "E":
            elevations[-1].append(char)
        elif char == "S":
            elevations[-1].append("a")
            start = [x, y]
        elif char == "E":
            elevations[-1].append("z")
            end = [x, y]

adjacencyMatrix = np.array([[0 for _ in range(len(elevations) * len(elevations[0]))]
                            for _ in range(len(elevations) * len(elevations[0]))]).T
for x, elevationCol in enumerate(elevations):
    for y, elevation in enumerate(elevationCol):
        currLoc = y * len(elevations) + x
        print(currLoc, len(elevations), len(elevations[0]))
        if x < len(elevations[0]) - 1:
            result = int(ord(elevation) - ord(elevations[x+1][y]) >= -1)
            adjacencyMatrix[currLoc][currLoc + 1] = result
            print(result)
        if x > 0:
            result = int(ord(elevation) - ord(elevations[x-1][y]) >= -1)
            adjacencyMatrix[currLoc][currLoc - 1] = result
            print(result)
        if y < len(elevations):
            result = int(ord(elevation) - ord(elevations[x][y+1]) >= - 1)
            adjacencyMatrix[currLoc][currLoc + len(elevations[0])] = result
            print(result)
        if y > 0:
            result = int(ord(elevation) - ord(elevations[x][y-1]) >= - 1)
            adjacencyMatrix[currLoc][currLoc - len(elevations[0])] = result
            print(result)

print(elevations)
print(np.array(adjacencyMatrix))
print(adjacencyMatrix[0])
print(start)
print(end)


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print((node % len(elevations[0]), node //
                  len(elevations[0])), "\t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
        min_index = -1
        # Initialize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)
        return end[0] + end[1] * len(elevations)


print(len(elevations) * len(elevations[0]))
g = Graph(len(elevations) * len(elevations[0]))
g.graph = adjacencyMatrix
ans = g.dijkstra(start[0] + start[1] * len(elevations))
print(np.array(elevations))
print(ans)
#submit(ans, part="a", day=12, year=2022)
