import string
from collections import deque

with open("inputs/day12.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]

# Setup
R = len(data)
C = len(data[0])
costs = {i: j for i, j in zip(string.ascii_lowercase, 
                              range(1, 27))}

S = (0, 0)
E = (0, 0)
nghbrs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i, row in enumerate(data):
    if "S" in row:
        S = (i, row.index("S"))
    if "E" in row:
        E = (i, row.index("E"))

cost_map = [[costs.get(j, 0) for j in i] for i in data]
cost_map[S[0]][S[1]] = 1
cost_map[E[0]][E[1]] = 26

def search(part):
    q = deque()
    for r in range(R):
        for c in range(C):
            if ((data[r][c] == "S" and part == 1) or 
                (data[r][c] == "a" and part == 2)):
                    q.append(((r,c), 0))
    
    visited = set()
    while q:
        (r,c), d = q.popleft()
        if (r,c) in visited:
            continue
        visited.add((r,c))
        if data[r][c] == "E":
            return d
        for dr, dc in nghbrs:
            rr = r + dr
            cc = c + dc
            if ((0<=rr<R) and (0<=cc<C) and 
                (cost_map[rr][cc]<=cost_map[r][c]+1)):
                    q.append(((rr, cc), d+1))
                
print(search(1))
print(search(2))
        

