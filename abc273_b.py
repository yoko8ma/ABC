x, k = map(int, input().split())

for i in range(k):
  b = 10 ** (i+1)
  m = x % b
  # print(f'{m=}')
  m = int(str(m)[0])
  # print(f'{m=}')

  if m < 5:
    # 2048 // 10 = 204
    x = (x // b) * b
  else:
    x = ((x // b)+1) * b

  # print(f'{x=}')

print(x)
