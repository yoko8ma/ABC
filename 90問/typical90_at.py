import collections

def mod(a):
  return a%46

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a = collections.Counter(list(map(mod, a)))
b = collections.Counter(list(map(mod, b)))
c = collections.Counter(list(map(mod, c)))

ans = 0
h = []

for i in range(46):
  for j in range(46):
    for k in range(46):
      if (i+j+k)%46==0:
        h.append([i,j,k])

ans = 0

for x in h:
  ans += a[x[0]] * b[x[1]] * c[x[2]]

print(ans)
