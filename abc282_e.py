import itertools

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

for i in range(n-1):

  c = list(itertools.combinations(a, 2))
  mxs = []

  for p in c:
    x = p[0]
    y = p[1]
    mm = (x**y + y**x) % m
    mxs.append(mm)

  print(mxs)
  mv = max(mxs)
  print(mv)
  mi = mxs.index(mv)

  ans += mv
  print(ans)

  k = c[mi]
  print(k)
  a.remove(max(k))
  print(a)

print(ans)