with open("day9.txt") as f:
    data = [l.strip().split() for l in f.readlines()]

def move(x, d):
    if d == "L":
        x = (x[0], x[1]-1)
    elif d == "R":
        x = (x[0], x[1]+1)
    elif d == "U":
        x = (x[0]+1, x[1])
    else:
        x = (x[0]-1, x[1])
    return x

def adjust(x, y):
    """x is head, y is tail"""
    dr = x[0] - y[0]
    dc = x[1] - y[1]
    if abs(dr) <= 1 and abs(dc) <= 1:
        pass 
    # not sure this is possible:
    elif abs(dr) > 1 and abs(dc) > 1:
        y = (x[0]-1 if y[0]<x[0] else x[0]+1, 
             x[1]-1 if y[1]<x[1] else x[1]+1)
    elif abs(dr) > 1: # up or down
        y = (x[0]-1 if y[0]<x[0] else x[0]+1, x[1])
    elif abs(dc) > 1: # left or right
        y = (x[0], x[1]-1 if y[1]<x[1] else x[1]+1)
    else:
        pass # no other scenarios needed
    return y

# Part 1
visited = {}
h = (0, 0)
t = (0, 0)
for i in data:
    drxn, n = i
    n = int(n)
    for j in range(n):
        h = move(h, drxn)
        t = adjust(h, t)
        visited[t] = visited.get(t, 0) + 1
print(len(visited))    

# Part 2
visited = {}
h = (0, 0)
t = [(0, 0) for i in range(9)]
for i in data:
    drxn, n = i
    n = int(n)
    for j in range(n):
        h = move(h, drxn)
        t[0] = adjust(h, t[0])
        for k in range(1, 9):
            t[k] = adjust(t[k-1], t[k])
        visited[t[-1]] = visited.get(t[-1], 0) + 1
print(len(visited))
