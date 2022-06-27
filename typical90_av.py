n, k = map(int, input().split())

a =[]

for i in range(n):
  x, y = map(int, input().split())
  a.append(x-y)
  a.append(y)

a = sorted(a, reverse=True)
ans = sum(a[:k])
print(ans)
