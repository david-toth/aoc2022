with open("inputs/day10.txt") as f:
    data = [l.strip() for l in f.readlines()]

X = 1
cycles = []

for line in data:
    if line == "noop":
        cycles.append(X)
    else:
        _, n = line.split()
        n = int(n)
        cycles.append(X)
        cycles.append(X)
        X += n

print(sum((i)*cycles[i-1] for i in range(20, len(cycles), 40)))

img = ""
for i in range(0, len(cycles), 40):
    for j in range(40):
        pixel = "##" if abs(cycles[i+j] - j) <= 1 else "  "
        img += pixel
    img += "\n"

print(img)
        
    
        
        
        