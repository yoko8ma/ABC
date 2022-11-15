t = int(input())
l, x, y = map(int, input().split())
q = int(input())
e = [int(input()) for _ in range(q)]

for x in e:
  m = x % t
  if m <= t/2:
    pass