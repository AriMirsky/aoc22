from aocd import get_data, submit

input = get_data(day=8, year=2022)
lines = input.split("\n")

ans = 0
trees = []
for line in lines:
    trees.append([])
    for h in line:
        trees[-1].append(int(h))


def isVisible(trees, x, y):
    visible = False
    origx = x
    origy = y
    for i in range(x):
        if trees[origx][origy] <= trees[i][origy]:
            break
    else:
        visible = True

    for i in range(x + 1, len(trees)):
        if trees[origx][origy] <= trees[i][origy]:
            break
    else:
        visible = True

    for i in range(y):
        if trees[origx][origy] <= trees[origx][i]:
            break
    else:
        visible = True

    for i in range(y + 1, len(trees[0])):
        if trees[origx][origy] <= trees[origx][i]:
            break
    else:
        visible = True

    return visible


for r, row in enumerate(trees):
    for c, col in enumerate(row):
        if isVisible(trees, r, c):
            ans += 1

print(ans)
submit(ans, part="a", day=8, year=2022)
