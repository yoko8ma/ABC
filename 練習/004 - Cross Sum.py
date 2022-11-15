import numpy

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
# print(A)

for i in range(H):
  l = []
  for j in range(W):
    # print(A[i][j])
    # print(sum(A[i]))
    col_sum = sum(x[j] for x in A)
    # print(col_sum)
    l.append(sum(A[i]) + col_sum - A[i][j])

  print(*l)