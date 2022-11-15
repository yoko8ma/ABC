d = int(input())
n = int(input())

day = [0]*(d+1)

for i in range(n):
  l, r = map(int, input().split())
  day[l-1] += 1
  day[r] -= 1

ans = 0

for i in range(d):
  ans += day[i]
  print(ans)