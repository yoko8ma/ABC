n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = 0

ans = 0

while(l < n):
  # print(f'{l=}')
  # print(f'{r=}')
  # print(f'{a[l]=}')
  # print(f'{a[r]=}')

  if(r == n-1 or a[r] - a[l] > k):
    ans += r-1-l
    if r == n-1 and a[r] - a[l] <= k:
      ans += 1
    l += 1    
  else:
    r += 1

  print(f'{ans=}')

print(ans)
