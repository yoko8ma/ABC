import itertools

n, m = map(int, input().split())
a = [(input()) for _ in range(n)]

c = list(itertools.combinations(range(n), 2))
# print(c)

ans = 0

for pair in c:
  # print(pair)
  flag = True

  for i in range(m):
    if a[pair[0]][i] == 'x' and a[pair[1]][i] == 'x':
      flag = False

  if flag:
    ans += 1
  
print(ans)