with open("inputs/day14.txt") as f:
    data = [l.strip() for l in f.readlines()]

def parse_line(l):
    coords = []
    l = l.split(" -> ")
    for i in l:
        xy = i.split(",")
        coords.append(tuple(map(int, xy)))
    return coords

def draw_line(c1, c2):
    pts = []
    if c1[0] == c2[0]:
        if c1[1] < c2[1]:
            for i in range(c1[1], c2[1]+1):
                pts.append((c1[0], i))
        else:
            for i in range(c2[1], c1[1]+1):
                pts.append((c1[0], i))
    else:
        if c1[0] < c2[0]:
            for i in range(c1[0], c2[0]+1):
                pts.append((i, c1[1]))
        else:
            for i in range(c2[0], c1[0]+1):
                pts.append((i, c1[1]))
    return pts

#------- Part 1
pts = set()
for l in data:
    lp = parse_line(l)
    if len(lp) == 2:
        pts.update(draw_line(*lp))
    else:
        for i in range(1, len(lp)):
            pts.update(draw_line(*lp[i-1:i+1]))

ymax = max(i[1] for i in pts)
s = (500, 0)
sx, sy = s
nsand = 0

while True:
    blocked = True
    for dx, dy in [(0,1), (-1,1), (1,1)]:
        if (sx+dx, sy+dy) not in pts:
            sx += dx
            sy += dy
            blocked = False
            break
    if sy > 2*ymax:
        break
    if blocked:
        nsand += 1
        pts.add((sx, sy))
        sx, sy = s
        
print(nsand)

#-------- Part 2
pts = set()
for l in data:
    lp = parse_line(l)
    if len(lp) == 2:
        pts.update(draw_line(*lp))
    else:
        for i in range(1, len(lp)):
            pts.update(draw_line(*lp[i-1:i+1]))

ymax = max(i[1] for i in pts)

for x in range(-1000, 1000):
    pts.add((x, ymax+2))

s = (500, 0)
sx, sy = s
nsand = 0

while True:
    blocked = True
    for dx, dy in [(0,1), (-1,1), (1,1)]:
        if (sx+dx, sy+dy) not in pts:
            sx += dx
            sy += dy
            blocked = False
            break
    if blocked:
        nsand += 1
        if (sx, sy) == s:
            break
        pts.add((sx, sy))
        sx, sy = s
        
print(nsand)