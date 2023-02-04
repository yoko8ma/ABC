from time import sleep

n, k = map(int, input().split())
a = list(map(int, input().split()))
q = int(input())

for _ in range(q):
  l, r = map(int, input().split())
  s = a[l-1:r]
  print(s)
  l = 0
  r = 1

  while(True):
    d = s[l] - s[r]
    print(d)
    if d == 0:
      l += 1
      r += 1

    for i in range(r, n-k):
      s[i] += d
    print(s)
    sleep(1)
    