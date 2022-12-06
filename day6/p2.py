from aocd import get_data, submit

input = get_data(day=6, year=2022)
input2 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
lines = input.split("\n")

ans = 0
for i in range(len(input) - 3):
    newpacket = True
    for j in range(14):
        for k in range(14):
            if j == k:
                continue
            if input[i+j] == input[i+k]:
                newpacket = False
    if newpacket:
        ans = i + 14
        break

print(ans)
submit(ans, part="b", day=6, year=2022)
