from collections import defaultdict

with open("inputs/day7.txt") as f:
    data = [l.strip() for l in f.readlines()]

# Part 1
all_files = defaultdict(int)
cwd = []

for i in data:
    txt = i.split()
    if txt[0] == "$":
        if txt[1] == "cd":
            if txt[2] == "..":
                cwd.pop()
            else:
                cwd.append(txt[2])
        else: # ls 
            continue
    elif txt[0] == "dir":
        continue
    else:
        for j in range(len(cwd)):
            all_files["/".join(cwd[:j+1])] += int(txt[0])

print(sum(v for v in all_files.values() if v <= 100000))

# Part 2
used_space = all_files["/"]
total_space = 70000000
free_space = total_space - used_space
needed_space = 30000000 - free_space
print(min(v for v in all_files.values() if v >= needed_space))