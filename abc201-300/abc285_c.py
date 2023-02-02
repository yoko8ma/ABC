s = input()
s = list(s)
s.reverse()

base = ord('A')
d = 0
ans = 0

for x in s:
  i = ord(x) - base + 1
  ans += i * 26**d
  d += 1
  
print(ans)