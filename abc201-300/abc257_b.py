n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

c = [0]*n

for i in a:
  c[i-1] = 1

print(a)

for x in l:
  print('位置',x)
  print('駒の位置', a)
  print('マス', c)

  i = a[x-1]
  print('対象の駒の位置', i)

  if i == n:
    print('端')
    continue

  if c[i] == 1:
    print('右にある')
    continue

  c[i] = 1
  c[i-1] = 0
  a[x-1] += 1

print(*a)
