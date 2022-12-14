from aocd import get_data, submit

input = get_data(day=9, year=2022)
input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
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

    def headPos(self):
        return [self.head[0], self.head[1]]


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
ropes = [Rope() for _ in range(9)]
prevPrevPoss = [[0, 0] for _ in range(9)]
prevPoss = [[0, 0] for _ in range(9)]
reached = set()
reached.add((0, 0))
for line in lines:
    cmds = line.split(" ")
    for _ in range(int(cmds[1])):
        ropes[0].move(dirConversion(cmds[0]))
        print(cmds)
        print(dirConversion(cmds[0]))
        for i in range(1, 9):
            ropes[i].move([ropes[i - 1].tailPos()[0] - ropes[i].headPos()
                          [0], ropes[i - 1].tailPos()[1] - ropes[i].headPos()[1]])
            print([ropes[i - 1].tailPos()[0] - ropes[i].headPos()[0],
                  ropes[i - 1].tailPos()[1] - ropes[i].headPos()[1]])
        for i in range(9):
            print(ropes[i].tail, ropes[i].head)
        print()
        reached.add(tuple(ropes[8].tailPos()))
ans = len(reached)
print(reached)
print(ans)
#submit(ans, part="b", day=9, year=2022)
