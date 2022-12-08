with open("inputs/day1.txt") as f:
    data = [l.strip() for l in f.readlines()]

# Part 1
calories = []
elf = 0
for i in data:
    if i == "":
        calories.append(elf)
        elf = 0
    else:
        elf += int(i)
print(max(calories))

# Part 2
print(sum(sorted(calories, reverse=True)[:3]))
