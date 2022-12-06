# Day 6, part 1
with open("inputs/day6.txt") as f:
    data = f.readlines()

data = data[0].strip()

for i in range(len(data)-4):
    x = data[i:i+4]
    if len(set(x)) == len(x):
        print(i+4)
        break

# Day 6, part 2
for i in range(len(data)-14):
    x = data[i:i+14]
    if len(set(x)) == len(x):
        print(i+14)
        break