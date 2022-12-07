from aocd import get_data, submit

input = get_data(day=7, year=2022)
input2 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
lines = input.split("\n")


class Folder():
    subfolders = []
    items = []
    name = "/"
    parent = None

    def __init__(self, subfolders, items, name, parent):
        self.subfolders = subfolders
        self.items = items
        self.name = name
        self.parent = parent


root = Folder([], [], "/", None)
currDir = root

for line in lines:
    cmds = line.split(" ")
    print("next line")
    if cmds[0] == "$":
        print("terminal command")
        if cmds[1] == "cd":
            if cmds[2] == "/":
                currDir = root
            elif cmds[2] == "..":
                currDir = currDir.parent
            else:
                for folder in currDir.subfolders:
                    if folder.name == cmds[2]:
                        currDir = folder
                        break
                else:
                    print(cmds, "No subfolders found to cd into")
        elif cmds[1] == "ls":
            pass
    elif cmds[0] == "dir":
        newfolder = True
        for folder in currDir.subfolders:
            if folder.name == cmds[1]:
                newfolder = False
        if newfolder:
            currDir.subfolders.append(Folder([], [], cmds[1], currDir))
    else:
        newfile = True
        for filesize, filename in currDir.items:
            if filename == cmds[1]:
                newfile = False
        if newfile:
            currDir.items.append((int(cmds[0]), cmds[1]))


def size(f):
    currsize = 0
    for folder in f.subfolders:
        currsize += size(folder)
    for isize, _ in f.items:
        currsize += isize
    return currsize


def appendAllFolders(currd, ans):
    print(ans)
    if size(currd) <= 100000:
        ans += size(currd)
    thisfoldersize = 0
    for folder in currd.subfolders:
        thisfoldersize += appendAllFolders(folder, 0)
    return ans + thisfoldersize


minfoldersize = 70000000
delneeded = size(root) - 40000000


def findminfolder(currd, minfoldersize):
    if size(currd) < minfoldersize and size(currd) >= delneeded:
        minfoldersize = size(currd)
    for folder in currd.subfolders:
        minfoldersize = findminfolder(folder, minfoldersize)
    return minfoldersize


ans = findminfolder(root, minfoldersize)


print(ans)
submit(ans, part="b", day=7, year=2022)
