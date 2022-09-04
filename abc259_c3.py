s = list(input())
t = list(input())

def tr(l):
  a = []
  b = []

  for x in l:
    if len(b) == 0 or x in b:
      b.append(x)
    else:
      a.append(b)
      b = [x]
  a.append(b)

  return a

ns = tr(s)
nt = tr(t)


if (len(s) != len(t)):
  print('No')  
else:
  flg = True

  for i in len(ns):
    if ns[i] == nt[i]:
      continue

    if len(ns[i]) > len(nt[i]):
      flg = False
      break

    if len(ns[i]) == 1 and len(nt[i]) > 1:
      flg = False
      break

  if flg:
    print('Yes')
  else:
    print('No')
