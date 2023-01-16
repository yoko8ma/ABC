n = int(input())

for _ in range(n):
  n = int(input())
  a = list(map(int, input().split()))
  ans = sum(x%2==1 for x in a)
  print(ans)