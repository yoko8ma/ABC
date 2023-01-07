n = int(input())

for _ in range(n):
  n = int(input())
  a = list(map(int, input().split()))
  n = sum(x%2==1 for x in a)