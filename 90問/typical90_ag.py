import math

h, w = map(int, input().split())
print(h,w)

a = math.ceil(h / 2)
b = math.ceil(w / 2)
if h == 1:
  print(w)
elif w == 1:
  print(h)
else:
  print(a*b)
