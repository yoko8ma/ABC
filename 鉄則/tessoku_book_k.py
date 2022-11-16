import bisect

n, x = map(int, input().split())
a = list(map(int, input().split()))

i = bisect.bisect_left(a, x)
print(i+1)

# l = 0
# r = n-1

# while l<=r:
#   m = int((l+r) / 2)
  
#   if x < a[m]:
#     r = m -1
#   elif x == a[m]:
#     print(m+1)
#     break
#   else:
#     l = m + 1
