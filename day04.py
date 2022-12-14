# Day 4, part 1
with open("inputs/day4.txt") as f:
    data = [line.strip() for line in f.readlines()]
    data = [j.split("-") for i in data for j in i.split(",")]

pairs = [tuple(map(int, i)) for i in data]
total = 0
for i in range(0, len(pairs), 2):
    a, b = pairs[i:i+2]
    if ((min(a) <= min(b) and max(a) >= max(b)) or 
        (min(b) <= min(a) and max(b) >= max(a))):
        total += 1
print(total)

# Day 4, part 2
total = 0
for i in range(0, len(pairs), 2):
    a, b = pairs[i:i+2]
    ra, rb = (list(range(min(a), max(a)+1)), 
              list(range(min(b), max(b)+1)))
    if len(set(ra+rb)) < len(ra)+len(rb):
        total += 1
print(total)