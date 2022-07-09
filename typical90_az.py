import itertools

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