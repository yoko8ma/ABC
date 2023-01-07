s = [input() for _ in range(10)]

h = 0
flag = False

for i, l in enumerate(s):
  if '#' in l:
    a = i
    break

for i, l in enumerate(reversed(s)):
  if '#' in l:
    b = i
    break
b = 9-b

c = s[a].find('#')
d = s[a].rfind('#')

print(f'{a+1} {b+1}')
print(f'{c+1} {d+1}')
