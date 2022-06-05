import math
n = int(input())
mxd = len(str(n))

a = 0
for i in range(1, int(math.sqrt(n))+1):
  if n%i == 0:
    ad = len(str(i))
    bd = len(str(n//i))
    mx = max(ad, bd)
    if mx < mxd:
      mxd = mx
print(mxd)
