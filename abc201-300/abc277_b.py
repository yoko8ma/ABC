n = int(input())
s = [input() for _ in range(n)]

# print(s)

flag = True

for x in s:
  t = x[0]
  if not t in ['H', 'D', 'C', 'S']:
    flag = False
    break

  t = x[1]
  if not t in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
    flag = False
    break

s2 = list(set(s))

if len(s) != len(s2):
  flag = False

if flag:
  print('Yes')
else:
  print('No')

