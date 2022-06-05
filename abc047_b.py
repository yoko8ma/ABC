W, H, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
print(A)
l = []
for i in range(W):
  for j in range(H):
    l.append([i,j])
print(l)
ls = set(l)
for a in A:
  m = []
  if a[2] == 1:
    for x in range(m[0]):
      for y in range(H):
        m.append([x, y])
  ls = ls - set(m)

print(ls)