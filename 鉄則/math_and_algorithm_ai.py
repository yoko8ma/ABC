n, q = map(int, input().split())
a = list(map(int, input().split()))
l = [0]*q
r = [0]*q

for i in range(q):
  l[i], r[i] = map(int, input().split())

sum = [0]*n
sum[0] = a[0]

for i in range(1, n):
  sum[i] = sum[i-1] + a[i]

# print(sum)

for i in range(q):
  if l[i] == 1:
    print(sum[r[i]-1])
  else:
    print(sum[r[i]-1] - sum[l[i]-2])
