def func(n, y):
  for i in range(n+1):
    for j in range(n+1-i):
      k = n-i-j
#      print(i,j,k)
      m = 10000*i + 5000*j + 1000*k
#      print(m)
      if m == y:
        print(i,j,k)
        return
  print(-1,-1,-1)

n, y = map(int, input().split())
func(n, y)
