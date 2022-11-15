from doctest import master
import math

a, b, c = map(int, input().split())

# if b * math.log(c, 2) - math.log(a, 2) > 0:
if c**b - a > 0:
  print('Yes')
else:
  print('No')