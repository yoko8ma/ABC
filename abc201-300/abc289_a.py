s = input()
ans = ''

for x in s:
  if x == '0':
    ans += '1'
  else:
    ans += '0'

print(ans)
