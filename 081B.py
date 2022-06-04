n = int(input())
a = list(map(int, input().split()))
i = 0
while True:
  m = [n%2 for n in a]

  if 1 in m:
    break
  else:
    i += 1
    
  a = [n//2 for n in a]
print(i)