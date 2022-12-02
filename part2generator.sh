#!/usr/bin/bash

cd "/home/ari/Documents/aoc/day${1}"
cp p1.py p2.py
sed -i '$d' p2.py
echo "#submit(ans, part=\"b\", day=${1}, year=2022)" >> p2.py