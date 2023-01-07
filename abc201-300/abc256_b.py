n = int(input())
a = list(map(int, input().split()))

b = [0]*4
p = 0

for i in range(n):
  # print(f'{i=}')
  b[0] = 1

  for j in [3, 2, 1, 0]:
    # print(f'{j=}')
    # print(f'{b[j]=}')

    if b[j] == 1:
      b[j] = 0
      t = j + a[i]
      # print(f'{t=}')

      if t > 3:
        p += 1
      else:
        b[t] = 1

    # print(f'{b}')
print(p)
