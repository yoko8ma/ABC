import itertools
n = int(input())

s = format(n, 'b')
s = list(map(int, str(s)))

a = []

for x in s:
  if x == 0:
    a.append(['0'])
  else:
    a.append(['0', '1'])

ans = []

p = itertools.product(*a)
for v in p:
    t = ''.join(v)
    print(int(t, 2))
