#!/usr/bin/bash

cd /home/ari/Documents/aoc
for i in {3..25}
do
    CURRPATH="day${i}"
    mkdir $CURRPATH
    echo "from aocd import get_data, submit

input = get_data(day=${i}, year=2022)
lines = input.split(\"\\n\")

ans = 0
for line in lines:
    pass

print(ans)
#submit(ans, part=\"a\", day=${i}, year=2022)" > "${CURRPATH}/p1.py"
done