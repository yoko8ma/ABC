N = int(input())
ma = []
for i in range(1, int(N/2)+1):
  print(i, N-i)
  a = i
  b = N-i
  aa = [int(x) for x in str(a)]
  ba = [int(x) for x in str(b)]
  print(aa)
  print(ba)
  ma.append(sum(aa)+sum(ba))
print(ma)
print(min(ma))