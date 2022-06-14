x, a, d, n = map(int, input().split())

if d == 0:
  print(abs(x-a))
else:
  print(f'x:{x}')
  print(f'a:{a}')
  print(f'd:{d}')
  h = (x-a)/d
  if h < 0:
    print(abs(x-a))
  else:
    print(f'index:{h}')
    
    if h > n-1:
      print('over')
      h = n-1

    if h%1 < 0.5:
      h = int(h//1)
    else:
      h = int(h//1+1)

    print(f'index near:{h}')
    l = a + d*h
    print(f'target:{l}')
    print(abs(l-x))
