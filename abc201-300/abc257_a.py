n, x = map(int, input().split())
q, m = divmod(x, n)

s = ''

for i in range(26):
  for j in range(n):
    s += chr(ord('A') + i)

print(s)
print(s[x-1])
