n = int(input())
s = input()

for i in range(1, n):
  x = 0

  for j in range(n-i):
    if s[j] == s[j+i]:
      break

    x += 1

  print(x)