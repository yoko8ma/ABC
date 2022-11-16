h, w = map(int, input().split())

mt = [[0] * (h+1) for i in range(w+1)]

for i in range(h):
  x = list(map(int, input().split()))

  for j in range(w):
    for k in range(i, h):
      for l in range(j, w):
        # print(f'{i=}')
        # print(f'{j=}')
        # print(f'{k=}')
        # print(f'{x[j]=}')
        mt[k+1][l+1] += x[j]
        # print(f'{mt=}')

# print(mt)
q = int(input())

for _ in range(q):
  a, b, c, d = map(int, input().split())
  # print(mt[c][d] + mt[a-1][b-1])
  # print(mt[c][b-1])
  # print(mt[a-1][d])
  print(mt[c][d] + mt[a-1][b-1] - mt[c][b-1] - mt[a-1][d])