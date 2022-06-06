n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(n,k,a,b)
d = 0
for i in range(n):
  d += abs(a[i] - b[i])

z = k - d
if z < 0:
  print('No')
elif z == 0:
  print('Yes')
else:
  if z%2 == 0:
    print('Yes')
  else:
    print('No')
