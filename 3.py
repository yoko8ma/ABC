import copy

N, K = map(int, input().split())
A = list(map(int, input().split()))
oA = copy.copy(A)
# print(N, K, A)
# print(N-K)

pA = copy.copy(A)
li = 50
cnt = 0
while True:
  for i in range(N-K):
    i += cnt
    # print(A[i], A[i+K])
    if A[i] > A[i+K]:
      s = A[i]
      A[i] = A[i+K]
      A[i+K] = s
      # print(A)
  # print(A)
  # if A == pA:
  #   break
  # else:
  # print(cnt, li)
  cnt += 1
  if cnt >= N-K:
    break
  pA = copy.copy(A)

  # print(sorted(A))
if (A == sorted(oA)):
  print('Yes')
else:
  print('No')
