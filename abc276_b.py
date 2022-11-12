n, m = map(int, input().split())
a = [0]*m
b = [0]*m

for i in range(m):
  a[i], b[i] = map(int, input().split())

# print(a, b)

d = {}

for i in range(n):
  d[i+1] = []

# print(d)

for i in range(m):
  v = d[a[i]]
  # print(f'{a[i]=}')
  # print(f'{b[i]=}')
  v.append(b[i])
  # print(f'{v=}')
  d[a[i]] = v

  v = d[b[i]]
  v.append(a[i])
  d[b[i]] = v

  # print(f'{d=}')
  
# print(d)

for k, v in d.items():
  # print(k, v)
  x = sorted(v)
  x = [str(i) for i in x]
  print(f'{len(v)} {" ".join(x)}')