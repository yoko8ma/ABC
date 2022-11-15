def func(N):
  # print(N)
  mx4 = N//4
  mx7 = N//7

  for i in range(mx4+1):
    for j in range(mx7+1):
      if 4*i + 7*j == N:
        return True

  return False

N = int(input())
res = func(N)

if res:
  print('Yes')
else:
  print('No')
