s = [input() for _ in range(9)]
print(s)

flag = False
pi = 0
pj = 0
ans = 0

for i in range(9):
  for j in range(9):
    if s[i][j]=='#':
      print(f'{i=}')
      print(f'{j=}')
      print(f'{flag=}')

      if flag:
        ai = abs(i - pi)
        aj = abs(j - pj)
        # print(f'{ai=}')
        # print(f'{aj=}')

        print(s[i][j + ai])
        print(s[i + aj][j])
        if s[i][j + ai] == '#' and s[i + aj][j] == '#':
          ans += 1
          print(f'{ans=}')
          flag = False
      else:
        pi = i
        pj = j
        flag = True

print(ans)

