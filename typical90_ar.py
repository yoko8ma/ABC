n, q = map(int, input().split())
a = list(map(int, input().split()))
t = [list(map(int, input().split())) for _ in range(q)]
i = list(range(n))
# print(n,q,a,t)
bp = 0

for x in t:
  if x[0] == 1:
    ai = (x[1]-1-bp+n)%n
    bi = (x[2]-1-bp+n)%n
    i[ai], i[bi] = i[bi], i[ai]
  elif x[0] == 2:
    bp += 1
  else:
    ai = x[1]-1-bp
    if ai > n-1:
      ai -= n-1
    print(a[i[ai]])
