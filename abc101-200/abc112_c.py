def func(n, a):
  b = None
  for x in a:
    if x[2] != 0:
      b = x

  for i in range(101):
    for j in range(101):
        h = b[2] + abs(b[0]-i) + abs(b[1]-j)
        flag = True
        
        for m in a:
          if m[2] != max(h - abs(m[0]-i)- abs(m[1]-j), 0):
            flag = False
            break
        if flag:
          return i, j, h

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
print(*(func(n,a)))
