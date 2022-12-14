from aocd import get_data, submit

input = get_data(day=6, year=2022)
input2 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
lines = input.split("\n")

ans = 0
for i in range(len(input) - 3):
    newpacket = True
    for j in range(4):
        for k in range(4):
            if j == k:
                continue
            if input[i+j] == input[i+k]:
                newpacket = False
    if newpacket:
        ans = i + 4
        break

print(ans)
submit(ans, part="a", day=6, year=2022)
