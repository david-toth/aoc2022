# Day 1, Part 1
with open("inputs/day1.txt") as f:
    lines = f.readlines()

cals = []
elf = []
for line in lines:
    if line == '\n':
        cals.append(elf)
        elf = []
    else:
        elf.append(int(line.strip()))

print(max([sum(i) for i in cals]))

# Day 1, part 2
print(sum(sorted([sum(i) for i in cals], reverse=True)[:3]))