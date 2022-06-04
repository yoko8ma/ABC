import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
# print(X)

cnt = 0

for i in range(N-1):
  # print(X[i])
  for j in range(i+1, N):
    # print(X[j])
    d = 0
    for k in range(D):
      d += (X[i][k]-X[j][k]) ** 2
    # print(d)
    d = math.sqrt(d)  
    # print(d)
    # print(int(d) - d)
    if int(d) - d == 0:
      cnt += 1

print(cnt)