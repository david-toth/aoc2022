#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

with open("day8.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]
data = [list(map(int, i)) for i in data]
x = np.array(test)

total = 0
for i in range(1, len(x)-1):
    for j in range(1, len(x[0])-1):
        y = x[i, j]
        left = all(y > x[i, :j])
        right = all(y > x[i, j+1:])
        up = all(y > x[:i, j])
        down = all(y > x[i+1:, j])
        total += int(any((left, right, up, down)))
print(total + (2*x.shape[0] + 2*x.shape[1] - 4))

def check_direction(x, dlist, reverse=False):
    score = 0
    if reverse:
        dlist = dlist[::-1]
    for i in dlist:
        score += 1
        if i >= x:
            break
    return score

max_score = 1
for i in range(1, len(x)-1):
    for j in range(1, len(x[0])-1):
        c = x[i, j]
        left = x[i, :j]
        lscore = check_direction(c, left, True)
        right = x[i, j+1:]
        rscore = check_direction(c, right)
        up = x[:i, j]
        uscore = check_direction(c, up, True)
        down = x[i+1:, j]
        dscore = check_direction(c, down)
        score = lscore*rscore*uscore*dscore
        if score > max_score:
            max_score = score
print(max_score)


# In[ ]:




