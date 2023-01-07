n, m = map(int, input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]

cnt = 0
for x in s:
  cnt += len(x)
print(cnt)
c = 16 - cnt
