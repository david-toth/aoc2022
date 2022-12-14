with open("inputs/day14.txt") as f:
    data = [l.strip() for l in f.readlines()]
    
def parse_line(l):
    c = []
    for i in l.split(" -> "):
        for j in i.split(","):
            c.append(tuple(map(int, j)))
   return c

def build_lines(c1, c2):
    p = []
    if c1[0] == c2[0]:
        if c1[1] < c2[1]:
            a = c1[1]
            b = c2[1] + 1
        else:
            a = c2[1]
            b = c1[1] + 1
        for i in range(a, b):
            p.append((c1[0], i))
    else:
        if c1[0] < c2[]:
            a = c1[0]
            b = c2[0] + 1
        else:
            a = c2[0]
            b = c1[0] + 1
        for i in range(a, b):
            p.append((i, c1[1]))
    return p

pts = set()

# Find points 
for l in data:
    pl = parse_line(l)
    if len(pl) == 2:
        pts.update(build_lines(pl[0], pl[1]))
    else:
        for i in range(1, len(pl)):
            pts.update(build_lines(pl[i-1], pl[i]))

ymax = max(i[1] for i in pts)
sand = (500, 0)
sx, sy = sand
num_particles = 0
#-------------- Part 1
while True:
    blocked = True
    for dx, dy in ((0, 1), (1, 1), (-1, 1)):
        if (sx+dx, sy+dy) not in pts:
            sx += dx
            sy += dy
            blocked = False
            break
    if sy > 2*ymax: # assume abyss is anything > double the deepest rock
        break 
    if blocked:
        num_particles += 1
        pts.add((sx, sy))
        sx, sy = sand
        
print(num_particles)
#-------------- Part 2
pts = set()

# Find points 
for l in data:
    pl = parse_line(l)
    if len(pl) == 2:
        pts.update(build_lines(pl[0], pl[1]))
    else:
        for i in range(1, len(pl)):
            pts.update(build_lines(pl[i-1], pl[i]))

ymax = max(i[1] for i in pts)
sand = (500, 0)
sx, sy = sand
num_particles = 0

for x in (-1000, 1000):
    pts.add((x, ymax+2))
    
while True:
    blocked = True
    for dx, dy in ((0, 1), (1, 1), (-1, 1)):
        if (sx+dx, sy+dy) not in pts:
            sx += dx
            sy += dy
            blocked = False
            break
    if blocked:
        num_particles += 1
        if (sx, sy) == sand:
            break
        pts.add((sx, sy))
        sx, sy = sand
        
print(num_particles)
