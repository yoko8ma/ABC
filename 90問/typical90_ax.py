import math

def combinations_count(n, r):
    if n-r < 0:
      return 1

    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n, l = map(int, input().split())

q, m = divmod(n, l)
if m>0:
  q += 1
ans = 0

for i in range(q+1):
  # print(l, "段飛び", i, "回")
  aida = n - i*l
  if aida < 0:
    aida = 0
  aida = aida*i
  # print("1段飛び", aida, "回")
  c = combinations_count(aida+1, i)
  # print("組み合わせ", c)
  ans += c

print(int(ans%(10**9+7)))
