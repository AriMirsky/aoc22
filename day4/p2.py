from aocd import get_data, submit

input = get_data(day=4, year=2022)
lines = input.split("\n")

ans = 0
for line in lines:
    elfs = line.split(",")
    elfs = [elfs[0].split("-"), elfs[1].split("-")]

    if (int(elfs[0][1]) >= int(elfs[1][0]) and int(elfs[0][0]) <= int(elfs[1][1])):
        ans += 1
print(ans)
submit(ans, part="b", day=4, year=2022)
