# Day 3, part 1
import string

with open("inputs/day3.txt") as f:
    data = [line.strip() for line in f.readlines()]

def parse(line):
    n = len(line)
    mid = n // 2
    left, right = set(line[:mid]), set(line[mid:])
    return [i for i in left if i in right][0]

results = list(map(parse, data))
priority = {j: i for i, j in enumerate(string.ascii_letters, 1)}
print(sum(priority[i] for i in results))

# Day 3, part 2
total = 0
for i in range(0, len(data), 3):
    (letter,) = set.intersection(*list(map(set, data[i:i+3])))
    total += priority[letter]
print(total)