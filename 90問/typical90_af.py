import itertools

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 10**10

for v in itertools.permutations(range(n), n):
  flag = False
  for x in range(len(v)-1):
    print([v[x], v[x+1]])
    if [v[x], v[x+1]] in xy:
      flag = True
      break
  if flag:
    continue

  print(v[1])
  s = 0
  for i in range(n):
    s += a[i][v[i]]
  ans = min(ans, s)

print(ans)