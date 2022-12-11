from aocd import get_data, submit

input = get_data(day=9, year=2022)
lines = input.split("\n")


class Rope():
    def __init__(self):
        self.tail = [0, 0]
        self.head = [0, 0]

    def move(self, direction):
        self.head[0] += direction[0]
        self.head[1] += direction[1]

        if self.tail[0] >= self.head[0] + 2:
            self.tail[0] = self.head[0] + 1
            self.tail[1] = self.head[1]
        elif self.tail[0] <= self.head[0] - 2:
            self.tail[0] = self.head[0] - 1
            self.tail[1] = self.head[1]
        elif self.tail[1] >= self.head[1] + 2:
            self.tail[1] = self.head[1] + 1
            self.tail[0] = self.head[0]
        elif self.tail[1] <= self.head[1] - 2:
            self.tail[1] = self.head[1] - 1
            self.tail[0] = self.head[0]

    def tailPos(self):
        return [self.tail[0], self.tail[1]]


def dirConversion(dir):
    if dir == "R":
        return [1, 0]
    elif dir == "U":
        return [0, 1]
    elif dir == "L":
        return [-1, 0]
    elif dir == "D":
        return [0, -1]


ans = 0
ropes = [Rope() for _ in range(10)]
prevPrevPoss = [[0, 0] for _ in range(10)]
prevPoss = [[0, 0] for _ in range(10)]
reached = set()
reached.add((0, 0))
for line in lines:
    cmds = line.split(" ")
    for _ in range(int(cmds[1])):
        ropes[0].move(dirConversion(cmds[0]))
        print(cmds)
        print(dirConversion(cmds[0]))
        for i in range(1, 10):
            ropes[i].move([-prevPrevPoss[i - 1][0] + ropes[i - 1].tailPos()
                          [0], -prevPrevPoss[i - 1][1] + ropes[i - 1].tailPos()[1]])
            print([-prevPrevPoss[i - 1][0] + ropes[i - 1].tailPos()
                   [0], -prevPrevPoss[i - 1][1] + ropes[i - 1].tailPos()[1]])
        for i in range(10):
            prevPrevPoss[i] = prevPoss[i]
            prevPoss[i] = ropes[i].tailPos()
            print(ropes[i].tail, ropes[i].head,
                  "     ", prevPrevPoss[i], prevPoss[i])
        print()
        reached.add(tuple(ropes[9].tailPos()))
ans = len(reached)
print(ans)
#submit(ans, part="b", day=9, year=2022)
