n = int(input())
a, b, c = map(int, input().split())

ans = 9999
l = 9999

for i in range(l+1):
  for j in range(l+1-i):
    s = n - a*i - b*j
    if s < 0:
      break
    k, m = divmod(n - a*i - b*j, c)
    if m != 0:
      continue
    
    ans = min(ans, i+j+k)

print(ans)
