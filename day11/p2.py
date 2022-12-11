from aocd import get_data, submit
from math import gcd

input = get_data(day=11, year=2022)
input2 = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

lines = input.split("\n")


class Monkey():
    def __init__(self, items, operation, test, iftrue, iffalse, testDivis):
        self.items = items
        self.operation = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.testDivis = testDivis


ans = 0
monkeys = []
currMonkey = None
currItems = None
currOperation = None
currTest = None
currIfTrue = None
currIfFalse = None
currTestDivis = None
for line in lines:
    cmds = line.split(" ")
    # print(cmds)
    if cmds[0] == "Monkey":
        currMonkey = cmds[1]
        continue
    if not(len(line) > 0 and line[0:2] == "  "):
        monkeys.append(Monkey(currItems, currOperation,
                       currTest, currIfTrue, currIfFalse, currTestDivis))
        continue
    # Indent
    cmds = cmds[2:]
    if cmds[0] == "Starting":
        items = []
        for i in cmds[2:]:
            items.append(int(i.strip(",")))
        currItems = items
    elif cmds[0] == "Operation:":
        op = None
        # print(cmds)
        if cmds[5] != "old":
            operand = int(cmds[5])
        if cmds[4] == "*":
            #print("Special", cmds)
            if cmds[5] != "old":
                def op(operand):
                    def closure(x):
                        return x * operand
                    return closure
                op = op(operand)
            else:
                def op(x): return x * x
        elif cmds[4] == "+":
            def op(operand):
                def closure(x):
                    return x + operand
                return closure
            op = op(operand)
        currOperation = op
    elif cmds[0] == "Test:":
        # print(cmds)
        num = int(cmds[3])

        def op(num):
            def closure(x):
                return x % num == 0
            return closure
        op = op(num)
        currTest = op

        currTestDivis = num
    else:
        cmds = cmds[3:]
        # print(cmds)
        if cmds[0] == "true:":
            currIfTrue = int(cmds[4])
        elif cmds[0] == "false:":
            currIfFalse = int(cmds[4])

monkeys.append(Monkey(currItems, currOperation,
               currTest, currIfTrue, currIfFalse, currTestDivis))

inspects = [0] * len(monkeys)

divistestnums = [0] * len(monkeys)

for i, monkey in enumerate(monkeys):
    divistestnums[i] = monkey.testDivis

lcm = 1
for i in divistestnums:
    lcm = lcm*i//gcd(lcm, i)

for round in range(10000):
    for monkeyi, monkey in enumerate(monkeys):
        while 0 < len(monkey.items):
            # print(monkey.items[0])
            monkey.items[0] = monkey.operation(monkey.items[0]) % lcm
            inspects[monkeyi] += 1

            # print(monkey.items[0])
            currItem = monkey.items[0]
            monkey.items = monkey.items[1:]
            if monkey.test(currItem):
                monkeys[monkey.iftrue].items.append(currItem)
            else:
                monkeys[monkey.iffalse].items.append(currItem)
        # print()
    for i, monkey in enumerate(monkeys):
        #print(i, monkey.items)
        # print()
        pass


max = 0
max2 = 0
for inspect in inspects:
    if inspect >= max:
        max2 = max
        max = inspect
    elif inspect >= max2:
        max2 = inspect

ans = max * max2

# print(inspects)
print(ans)
submit(ans, part="b", day=11, year=2022)
