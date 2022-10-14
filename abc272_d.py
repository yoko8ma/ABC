from math import floor, ceil
def min_mex(a, j):
  mx = max(a)

  cnt = [0] * (max(a)+len(a)+j+1)

  for i, x in enumerate(a):
    if x+i+j < 0:
      continue
    cnt[x+i+j] += 1


  if 0 in cnt:
    return cnt.index(0)+j
  else:
    return mx+j+1

n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(m):
  for j in range(n):
    a[j] += j+1
  # print(min_mex(a, j))
