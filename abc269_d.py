import numpy as np

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
solo = 0
s = []

for i, x in enumerate(a):
  flag = False

  if [x[0]-1, x[1]-1] in a:
    flag = True
    s.append([i, a.index([x[0]-1, x[1]])])

  if [x[0]-1, x[1]] in a:
    flag = True
    s.append([i, a.index([x[0]-1, x[1]])])

  if [x[0], x[1]-1] in a:
    flag = True
    s.append([i, a.index([x[0], x[1]-1])])

  if [x[0], x[1]+1] in a:
    flag = True
    s.append([i, a.index([x[0], x[1]+1])])

  if [x[0]+1, x[1]] in a:
    flag = True
    s.append([i, a.index([x[0]+1, x[1]])])

  if [x[0]+1, x[1]+1] in a:
    flag = True
    s.append([i, a.index([x[0], x[1]+1])])

  if not flag:
    solo +=1

print(solo)
s =  np.sort(s).tolist()
s = list(map(list, set(map(tuple, s))))
print(s)

for x in s:
  for y in x:
    print(y)