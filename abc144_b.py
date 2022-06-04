def func(N):
  for i in range(1, 10):
    for j in range(1, 10):
      if N == i * j:
        return True
  return False

N = int(input())
res = func(N)

if res:
  print('Yes')
else:
  print('No')
