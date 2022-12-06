# Day 5, part 1
import re

with open("inputs/day5.txt") as f:
    data = [line.strip() for line in f.readlines()]

split = data.index("")
instr = data[split+1:]

# This is my input stack
# Honestly easier for me to type it out in this case
stack = {
    1: "QHCTNSVB",
    2: "GBDW",
    3: "BQSTRWF",
    4: "NDJZSWGL",
    5: "FVDPM",
    6: "JWF",
    7: "VJBQNL",
    8: "NSQJCRTG",
    9: "MDWCQSJ"
}
stack_c = stack.copy()

for i in instr:
    # move n from stack a to stack b
    n, a, b = list(map(int, re.findall(r'\d+', i)))
    sa, sb = stack_c[a], stack_c[b]
    stack_c[a] = sa[n:]
    stack_c[b] = "".join(list(reversed(sa[:n]))) + sb
print("".join(v[0] for k,v in stack_c.items()))

# Day 5, part 2
for i in instr:
    # move n from stack a to stack b
    n, a, b = list(map(int, re.findall(r'\d+', i)))
    sa, sb = stack.get(a, ""), stack.get(b, "")
    stack[a] = sa[n:]
    stack[b] = "".join(list(sa[:n])) + sb
print("".join(v[0] for k,v in stack.items()))