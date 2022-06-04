N = int(input())
m = N%100
if m < 10:
  print(f'0{m}')
else:
  print(m)
