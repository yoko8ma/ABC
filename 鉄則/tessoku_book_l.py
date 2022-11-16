n, k = map(int, input().split())
a = list(map(int, input().split()))

def check(x):
  global n, a, k
  sum = 0
  
  for i in range(n):
    sum += int(x / a[i])

  if sum >= k:
    return True
  else:
    return False

l = 1
r = 1000000000

while l < r:
  mid = int((l+r) / 2)
  answer = check(mid)
  
  if answer:
    r = mid
  else:
    l = mid + 1

print(l)