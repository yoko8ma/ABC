from sys import flags


s = list(input())
n = list(map(int, s))

a = ''

if n[0] == 1:
  print('No')
else:
  if n[6] == 0:
    a += '0'
  else:
    a += '1'

  if n[3] == 0:
    a += '0'
  else:
    a += '1'

  if n[7] == 1 or n[1] == 1:
    a += '1'
  else:
    a += '0'

  if n[4] == 0:
    a += '0'
  else:
    a += '1'

  if n[8] == 1 or n[2] == 1:
    a += '1'
  else:
    a += '0'

  if n[5] == 0:
    a += '0'
  else:
    a += '1'

  if n[9] == 0:
    a += '0'
  else:
    a += '1'

  if a == '1111111':
    print('No')
  elif a == '0000000':
    print('No')
  elif '101' in a:
    print('Yes')
  elif '1001' in a:
    print('Yes')
  elif '10001' in a:
    print('Yes')
  elif '100001' in a:
    print('Yes')
  elif '1000001' in a:
    print('Yes')
  else:
    print('No')
