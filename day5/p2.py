from aocd import get_data, submit


def move(stacks, fromindex, toindex, count):
    stacks[toindex] = stacks[toindex] + stacks[fromindex][-count:]
    stacks[fromindex] = stacks[fromindex][:-count]
    return stacks


input = get_data(day=5, year=2022)
inputlines = 8
input2 = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
lines = input.split("\n")

ans = ""
stacks = [[], [], [], [], [], [], [], [], []]
linesparsed = 0
for line in lines:
    if linesparsed >= inputlines:  # FIXED
        break
    for i in range(1, len(stacks)*4, 4):  # FIXED
        # print(stacks)
        if line[i] != " ":
            stacks[int(i/4)].append(line[i])
    linesparsed += 1
for stack in stacks:
    stack.reverse()

print(stacks)

linesparsed = 0
for line in lines:
    if not(linesparsed <= inputlines + 1):  # FIXED
        nums = line.split(" ")
        count = int(nums[1])
        fromindex = int(nums[3]) - 1
        toindex = int(nums[5]) - 1
        print(count, fromindex, toindex)
        stacks = move(stacks, fromindex, toindex, count)
        print(stacks)
    linesparsed += 1

for stack in stacks:
    if len(stack) != 0:
        print("not taken")
        ans += stack.pop()
    else:
        print("taken")
        ans += " "

print(ans)
submit(ans, part="b", day=5, year=2022)
