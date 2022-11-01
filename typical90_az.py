import itertools

# a b
# d e
# (a*d + a*e + b*d + b*e) = (10^ + 7) * q +  ans
n = int(input())
a = []
for i in range(n):
  a.append(list(map(int, input().split())))

print(a)

ans = 1

for i in range(n):
  p = a[i][0] + a[i][1] + a[i][2] + a[i][3] + a[i][4] + a[i][5]
  ans *= p

print(ans%1000000007)