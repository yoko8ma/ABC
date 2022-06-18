import math

a, b = map(int, input().split())

g = math.gcd(a, b)
ans = a * b // g

if ans > 10**18:
  print('Large')
else:
  print(ans)
