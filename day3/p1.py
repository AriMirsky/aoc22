from aocd import get_data, submit

input = get_data(day=3, year=2022)
lines = input.split("\n")

ans = 0
for line in lines:
    mid = int(len(line)/2)
    f = set(line[0:mid])
    s = set(line[mid:])
    a = f.intersection(s)
    for i in a:
        if i.islower():
            ans += ord(i) - ord('a') + 1
        else:
            ans += ord(i) - ord('A') + 27

print(ans)
submit(ans, part="a", day=3, year=2022)
