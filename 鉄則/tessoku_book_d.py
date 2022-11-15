from collections import deque

n = int(input())

ans = deque()

while True:
  q, m = divmod(n, 2)
  ans.appendleft(str(m))
  if q == 0 or q == 1:
    ans.appendleft(str(q))
    break
  n = q

ans = list(ans)
ans = ''.join(ans)
ans = ans.zfill(10)
print(ans)
