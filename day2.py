# Day 2, part 1
with open("inputs/day2.txt") as f:
    data = [tuple(line.strip().split(" ")) for line in f.readlines()]

key = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Z"): 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}
pts = 0
for i in data:
    pts += key[i[-1]]
    if i in key:
        pts += key[i]
print(pts)

# Day 2, part 2
key = {
    ("A", "X"): 0 + 3,
    ("A", "Y"): 3 + 1,
    ("A", "Z"): 6 + 2,
    ("B", "X"): 0 + 1,
    ("B", "Y"): 3 + 2,
    ("B", "Z"): 6 + 3,
    ("C", "X"): 0 + 2,
    ("C", "Y"): 3 + 3,
    ("C", "Z"): 6 + 1
}
print(sum([key[i] for i in data]))