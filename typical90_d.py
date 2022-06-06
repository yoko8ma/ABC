h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
m = [0]*h

cs = [sum(x[i] for x in a) for i in range(w)]

for x in range(h):
  m[x] = sum(a[x])

s = [[0] * w for i in range(h)]

for x in range(h):
  for y in range(w):
      s[x][y] = m[x] + cs[y] - a[x][y]

for x in s:
    print(*x)