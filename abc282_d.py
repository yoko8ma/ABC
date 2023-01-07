import itertools

n, m = map(int, input().split())
s = []

for _ in range(m):
  a = list(map(int, input().split()))
  print(a)
  a.sort()
  print(a)
  s.append(a)

print(s)

c = list(itertools.combinations(range(n), 2))
print(c)

for p in s:
  print(p)
  c.remove(list(p))

print(c)
