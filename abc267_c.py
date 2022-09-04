n, m = map(int, input().split())
a = list(map(int, input().split()))

v = []

for i in range(n-m+1):
  # print(f'i:{i}')
  s = 0
  k = 1
  for j in range(m):
    print(f'a[i+m-1]{a[i+m-1]}')
    if a[i+m-1] < 0:
      break
    # print(f'j:{i+j}')
    s += a[i+j] * k
    k += 1
  # print(f's:{s}')
  v.append(s)

print(max(v))