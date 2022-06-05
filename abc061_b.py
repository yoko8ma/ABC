N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
print(A)
l = [0] * N
for i in A:
  print(i)
  l[i[0]-1] += 1
  l[i[1]-1] += 1
print(l)
for c in l:
  print(c)