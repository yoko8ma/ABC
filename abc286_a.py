n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))

ans = []

if p==1:
  pass
else:
  ans.extend(a[:p-1])
ans.extend(a[r-1:s])
ans.extend(a[q:r-1])
ans.extend(a[p-1:q])
ans.extend(a[s:])
print(*ans)
