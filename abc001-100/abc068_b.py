n = int(input())

i = 1
while True:
  c = i * 2
  if c > n:
    break
  else:
    i *= 2
print(i)