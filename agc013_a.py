n = int(input())
a = list(map(int, input().split()))
print(n,a)

if n < 3:
  print(1)
else:
  cnt = 1
  d = 0

  for i in range(1, n):
    if a[i] == a[i-1]:
      continue
    elif a[i] > a[i-1]:
      if d == 0:
        d = 1
      elif d == -1:
        d = 0
        cnt += 1
      else:
        continue
    else:
      if d == 0:
        d = -1
      if d == 1:
        d = 0
        cnt += 1
      else:
        continue
  print(cnt)
