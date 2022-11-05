n, q = map(int, input().split())
a = list(map(int, input().split()))
l = [0]*q
r = [0]*q
v = [0]*q

for i in range(q):
  l[i], r[i], v[i] = map(int, input().split())

# print(l, r, v)

for i in range(q):
  ans = 0

  # print(f'{l[i]-2=}')
  for i in range(l[i]-2):
    ans += abs(a[i] - a[i+1])

  # print(f'{l[i]-1=} {r[i]=}')
  for j in range(l[i]-1, r[i]):
    # print(f'{j=}')
    a[j] += v[i]
    if j + 1 >= n:
      break
    ans += abs(a[j] - a[j+1])

  # print(f'{r[i]=} {n=}')
  for k in range(r[i], n):
    if k + 1 >= n:
      break
    ans += abs(a[k] - a[k+1])
  
  print(ans)