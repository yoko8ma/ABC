import math

x, y, d = map(int, input().split())
c = math.cos(math.radians(d))
s = math.sin(math.radians(d))

print(x*c-y*s, x*s+y*c)
