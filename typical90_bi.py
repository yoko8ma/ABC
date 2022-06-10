q = int(input())
a = [list(map(int, input().split())) for _ in range(q)]
# print(q, a)
c = []

for x in a:
  print(x)
  if x[0] == 1:
    c.insert(0, x[1])
  elif x[0] == 2:
    c.append(x[1])
  else:
    print(c[x[1]-1])
  print(c)
