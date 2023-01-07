s = list(input())
t = list(input())

def tr(l):
  a = []

  for i in range(len(l)):
    cnt = 0

    if i == 0:
      (l[0], 1)
      continue

    if l[i-1] != l[i]:
      a.append(l[i])
    elif i >= 2 and l[i-2] != l[i]:
      a.append(l[i])

  return a

ns = tr(s)
nt = tr(t)

if (len(s) > len(t)):
  print('No')  
elif (ns == nt):
  print('Yes')
else:
  print('No')