n = int(input())
s = [input() for _ in range(n)]
print(n, s)

ss = set()

for i, x in enumerate(s):
  if x in ss:
    continue
  else:
    ss.add(x)
    print(i+1)    
