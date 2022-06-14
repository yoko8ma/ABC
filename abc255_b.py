import math

n, k = map(int, input().split())
ls = list(map(int, input().split()))
ps = [list(map(int, input().split())) for _ in range(n)]

x = []
d = []
bl = []
m = []

for p in ps:
  d = []
  for l in ls:
    d.append(math.sqrt((p[0] - ps[l-1][0])**2 + (p[1] - ps[l-1][1])**2))
  m.append(min(d))

print(max(m))
