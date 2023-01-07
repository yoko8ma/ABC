n, q = map(int, input().split())

l=[]
a=[]
s=[0]*q
t=[0]*q

for i in range(n):
  m = list(map(int, input().split()))
  l.append(m[0])
  a.append(m[1:])

for i in range(q):
  s[i], t[i] = map(int, input().split())

for i, x in enumerate(s):
  print(a[s[i]-1][t[i]-1])