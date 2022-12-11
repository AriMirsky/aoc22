from aocd import get_data, submit

input = get_data(day=9, year=2022)
lines = input.split("\n")


class Rope():
    tail = [0, 0]
    head = [0, 0]

    def __init__(self):
        pass

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
        return self.tail


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
rope = Rope()
reached = set()
reached.add((0, 0))
for line in lines:
    cmds = line.split(" ")
    for _ in range(int(cmds[1])):
        rope.move(dirConversion(cmds[0]))
        reached.add(tuple(rope.tailPos()))
ans = len(reached)
print(ans)
#submit(ans, part="b", day=9, year=2022)
