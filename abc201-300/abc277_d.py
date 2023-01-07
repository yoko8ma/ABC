n, m = map(int, input().split())
a = list(map(int, input().split()))

am = []

for x in a:
  am.append((x+1)%m)

ax = list(set(am))
print(f'{ax=}')

mi = 1000000000000000000000

for x in ax:
  # print(f'{x=}')
  aa = a.copy()
  aa.remove(x)
  
  while True:
    if x in aa:
      pass
    else:
      # print(f'{sum(aa)=}')
      mi = min(mi, sum(aa))
      break

print(mi)
