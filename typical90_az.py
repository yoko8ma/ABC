import itertools

# a b
# d e
# (a*d + a*e + b*d + b*e) = (10^ + 7) * q +  ans
n = int(input())
a = []
for i in range(n):
  a.append(list(map(int, input().split())))

print(a)

ans = 0

for x in itertools.product(*a):
  prod = 1
  for num in x:
    prod *= num

  ans += prod

print(ans%1000000007)