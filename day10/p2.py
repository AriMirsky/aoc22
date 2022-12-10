from aocd import get_data, submit

input = get_data(day=10, year=2022)

input2 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

input2 = """noop
addx 3
addx -5"""

lines = input.split("\n")

ans = ""
cycles = 0
x = 1


def checkCycle(cycle, x):
    if (cycle - 20) % 40 != 0:
        return None
    return cycle * x


def renderPixel(cycle, x, ans):
    pixel = ""
    if (cycle-1) % 40 == x - 1 or (cycle-1) % 40 == x or (cycle-1) % 40 == x + 1:
        pixel = "#"
    else:
        pixel = "."

    if (cycle - 1) % 40 == 0:
        ans += "\n"
    ans += pixel
    return ans


for line in lines:
    # print("line")
    cmd = line.split(" ")
    if "noop" == cmd[0]:
        #print(cmd, x)
        cycles += 1
        ans = renderPixel(cycles, x, ans)
    elif "addx" == cmd[0]:
        #print(cmd, x)
        cycles += 1
        ans = renderPixel(cycles, x, ans)
        cycles += 1
        ans = renderPixel(cycles, x, ans)
        x += int(cmd[1])

print(ans)
#submit(ans, part="b", day=10, year=2022)
