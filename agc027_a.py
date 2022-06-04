N, X = map(int, input().split())
A = list(map(int, input().split()))
print(N, X, A)
A.sort()
cnt = 0
for a in A:
  X -= a
  if X < 0:
    break
  else:
    cnt += 1
if X > 0:
  cnt -= 1
print(cnt)