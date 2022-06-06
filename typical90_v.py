import math

a, b, c = map(int, input().split())
print(a,b,c)

gcd = math.gcd(a, math.gcd(b, c))

print(a//gcd-1 + b//gcd-1 + c//gcd-1)
