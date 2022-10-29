n = int(input())
a = list(map(int, input().split()))

d = {}
a.sort(reverse=True)

for x in a:
  if x in d:
    v = d.get(x)
    v += 1
    d[x] = v
  else:
    d[x] = 1
print(f'{d=}')

for x in list(d.values()):
  print(x)

for _ in range(n-len(d)):
  print(0)