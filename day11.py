import re
from math import prod

with open("inputs/day11.txt") as f:
    data = [l.strip() for l in f.readlines()]

data = [i for i in data if i != ""]

def digits(x):
    return re.findall(r'[0-9]+', x)

n = 8
data2 = {i: {} for i in range(n)}

for i in range(0, len(data), 6):
    info = data[i:i+6]
    monkey_no = int(digits(info[0])[0])
    items = list(map(int, digits(info[1])))
    if len(items) == 0:
        continue
    data2[monkey_no]["items"] = items
    op_idx = info[2].index("old")
    op = info[2][op_idx:]
    test_no = int(digits(info[3])[0])
    monkey_a = int(digits(info[4])[0])
    monkey_b = int(digits(info[5])[0])
    data2[monkey_no]["op"] = op
    data2[monkey_no]["test_no"] = test_no
    data2[monkey_no]["monkey_a"] = monkey_a
    data2[monkey_no]["monkey_b"] = monkey_b

# Part 1
for _ in range(20):
    for i in data2:
        ma = data2[i]["monkey_a"]
        mb = data2[i]["monkey_b"]
        if len(data2[i]["items"]) == 0:
            continue
        for j in data2[i]["items"]:
            data2[i]["inspections"] = data2[i].get("inspections", 0) + 1
            old = j
            new = eval(data2[i]["op"]) // 3
            if new % data2[i]["test_no"] == 0:
                data2[ma]["items"].append(new)
            else:
                data2[mb]["items"].append(new)
        data2[i]["items"] = []
        
print(prod(sorted([data2[i]["inspections"] for i in data2])[-2:]))

# Part 2
data2 = {i: {} for i in range(n)}

for i in range(0, len(data), 6):
    info = data[i:i+6]
    monkey_no = int(digits(info[0])[0])
    items = list(map(int, digits(info[1])))
    if len(items) == 0:
        continue
    data2[monkey_no]["items"] = items
    op_idx = info[2].index("old")
    op = info[2][op_idx:]
    test_no = int(digits(info[3])[0])
    monkey_a = int(digits(info[4])[0])
    monkey_b = int(digits(info[5])[0])
    data2[monkey_no]["op"] = op
    data2[monkey_no]["test_no"] = test_no
    data2[monkey_no]["monkey_a"] = monkey_a
    data2[monkey_no]["monkey_b"] = monkey_b

mod = 1
for i in data2:
    mod *= data2[i]["test_no"]
    
for _ in range(10000):
    for i in data2:
        ma = data2[i]["monkey_a"]
        mb = data2[i]["monkey_b"]
        if len(data2[i]["items"]) == 0:
            continue
        for j in data2[i]["items"]:
            data2[i]["inspections"] = data2[i].get("inspections", 0) + 1
            old = j
            new = eval(data2[i]["op"])
            new %= mod
            if new % data2[i]["test_no"] == 0:
                data2[ma]["items"].append(new)
            else:
                data2[mb]["items"].append(new)
        data2[i]["items"] = []
        
print(prod(sorted([data2[i]["inspections"] for i in data2])[-2:]))
