from aocd import get_data, submit
import numpy as np

input = get_data(day=14, year=2022)
input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
lines = input.split("\n")

ans = 0
environment = np.empty((600, 200), dtype=str)
for line in lines:
    points = line.split(" ")[::2]
    p = points[0].split(",")
    p = [int(j) for j in p]
    points = points[1:]
    for point in points:
        point = point.split(",")
        point = [int(j) for j in point]

        if p[0] == point[0]:
            if p[1] < point[1]:
                for i in range(p[1], point[1] + 1):
                    print(1)
                    environment[p[0], i] = "#"
            else:
                for i in range(point[1], p[1] + 1):
                    print(2)
                    environment[p[0], i] = "#"
        else:
            if p[0] < point[0]:
                for i in range(p[0], point[0] + 1):
                    print(3)
                    environment[i, p[1]] = "#"
            else:
                for i in range(point[0], p[0] + 1):
                    print(4)
                    environment[i, p[1]] = "#"
        #print(p, point)
        #print(environment[494:504, 0:10])


def simsand(environment, sandloc):
    donesim = False
    if environment[sandloc[0], sandloc[1] + 1] != "#" and environment[sandloc[0], sandloc[1] + 1] != "o":
        environment[sandloc[0], sandloc[1]] = "."
        environment[sandloc[0], sandloc[1] + 1] = "o"
        sandloc[1] += 1
    elif environment[sandloc[0] - 1, sandloc[1] + 1] != "#" and environment[sandloc[0] - 1, sandloc[1] + 1] != "o":
        environment[sandloc[0], sandloc[1]] = "."
        environment[sandloc[0] - 1, sandloc[1] + 1] = "o"
        sandloc[1] += 1
        sandloc[0] -= 1
    elif environment[sandloc[0] + 1, sandloc[1] + 1] != "#" and environment[sandloc[0] + 1, sandloc[1] + 1] != "o":
        environment[sandloc[0], sandloc[1]] = "."
        environment[sandloc[0] + 1, sandloc[1] + 1] = "o"
        sandloc[1] += 1
        sandloc[0] += 1
    else:
        donesim = True
    return environment, sandloc, donesim


sandspawn = [500, 0]
sandloc = sandspawn
sandcount = 0
while(sandloc[1] < 190):
    environment, sandloc, donesim = simsand(environment, sandloc)
    print(environment[494:504, 0:10])
    if donesim:
        sandloc = sandspawn
        sandcount += 1
        continue

ans = sandcount

print(ans)
#submit(ans, part="a", day=14, year=2022)
