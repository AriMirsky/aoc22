from aocd import get_data, submit

input = get_data(day=3, year=2022)
lines = input.split("\n")

ans = 0
elf = 0
rucks = ["", "", ""]
for line in lines:
    rucks[elf] = line
    if elf == 2:
        f = set(rucks[0])
        s = set(rucks[1])
        t = set(rucks[2])
        a = f.intersection(s).intersection(t)
        for i in a:
            if i.islower():
                ans += ord(i) - ord('a') + 1
            else:
                ans += ord(i) - ord('A') + 27
    elf += 1
    if elf == 3:
        elf = 0

print(ans)
submit(ans, part="b", day=3, year=2022)
