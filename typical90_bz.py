n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
print(n, m, a)
c = [0]*n

for x in a:
  if x[0] < x[1]:
    c[x[1]-1] += 1
  elif x[0] > x[1]:
    c[x[0]-1] += 1

cnt = sum(x==1 for x in c)
print(cnt)
