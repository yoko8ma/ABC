n, m, x, t, d = map(int, input().split())

if m > x:
  print(t)
else:
  diff = m - x
  print(t + diff*d)
