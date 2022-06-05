x = [list(map(int, input().split())) for _ in range(3)]
print(x)
a = [0]*3
b = [0]*3
a[0] = 0
b[0] = x[0][0] - a[0]
b[1] = x[0][1] - a[0]
b[2] = x[0][2] - a[0]
a[1] = x[1][0] - b[0]
a[2] = x[2][0] - b[0]

flag = True
for i in range(3):
  for j in range(3):
    if x[i][j] != a[i] + b[j]:
      flag = False

if flag:
  print('Yes')
else:
  print('No')
