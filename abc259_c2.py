s = list(input())
t = list(input())

h = list('abcdefghijklmnopqrstuvwxyz')

flg = True

for x in h:
  s_cnt = s.count(x)
  t_cnt = t.count(x)

  if s_cnt == t_cnt:
    continue

  if s_cnt == 0 and t_cnt == 0:
    flg = False
    break

  if s_cnt > t_cnt:
    flg = False
    break

  if s_cnt == 1:
    flg = False
    break

if flg:
  print('Yes')
else:
  print('No')
