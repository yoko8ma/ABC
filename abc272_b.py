import itertools

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

l = []
for i in range(n):
  l.append(i+1)

# ペア
c = list(itertools.combinations(l, 2))
# print(c)

# 
x = []
for i in a:
  a = i[1:]
  b = list(itertools.combinations(a, 2))
  # print(b)

  for pi in b:
    if pi in c:
      c.remove(pi)

# print(c)
# print(len(c))

if len(c) == 0:
  print('Yes')
else:
  print('No')