n = int(input())
p = list(map(int, input().split()))
mx = []

for j in range(n):
  cnt = 0

  for i in range(n):
    x = [(i-1) % n, i, (i+1) % n]
    ix = p.index(i)
    if ix in x:
      cnt += 1

  mx.append(cnt)
  if cnt == n:
    break

  sw = p[0]
  for i in range(n-1):
    p[i] = p[i+1]
  p[n-1] = sw

print(max(mx))