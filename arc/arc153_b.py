h, w = map(int, input().split())

m = [[''] * w for i in range(h)]
ans = [['*'] * w for i in range(h)]

for i in range(h):
  s = input()
  for j in range(w):
    m[i][j] = s[j]

q = int(input())
a = [0]*q
b = [0]*q
for i in range(q):
  a[i], b[i] = map(int, input().split())

for i in range(q):
  # r1 左上
  for j in range(0, a[i]): # 縦
    ans[j][0] = m[a[i]-1-j][b[i]-1]

  for k in range(0, b[i]): # 横
    ans[0][k] = m[a[i]-1][b[i]-1-k]

  # r2 右上
  for j in range(0, a[i]): # 縦
    for k in range(b[i], w): # 横
      ans[j][k] = m[a[i]-1-j][b[i]-1-k]
  # r3 左下
  for j in range(a[i], h): # 縦
    for k in range(0, b[i]): # 横
      ans[j][k] = m[a[i]-1-j][b[i]-1-k]
  # r4 右下
  for j in range(a[i], h): # 縦
    for k in range(b[i], w): # 横
      ans[j][k] = m[a[i]-1-j][b[i]-1-k]

  for i in range(h):
    for j in range(w):
      m[i][j] = ans[i][j]

for x in ans:
    print(*x, sep='')

