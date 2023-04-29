h, w = map(int, input().split())

c = []

for i in range(h):
    s = input()
    m = list(s)
    c.append(m)

# a = np.array(a)
# print(c)
# print('---------------')
ss = []

for i in range(1, h-1):
    for j in range(1, w-1):
        # print(c[i][j])
        if c[i][j] == '#':
            if c[i-1][j-1] == '#' and c[i-1][j+1] == '#' and c[i+1][j-1] == '#' and c[i+1][j+1] == '#':
              # print(i, j)
              ss.append([i, j])

# print(s)
answer = [0] * min(h, w)

for s in ss:
  # print(s)
  d = 1
  i = s[0]
  j = s[1]

  while True:
    if i - d < 0:
      answer[d-2] += 1
      # print('枠外')
      break
    
    if c[i-d][j-d] == '#' and c[i-d][j+d] == '#' and c[i+d][j-d] == '#' and c[i+d][j+d] == '#':
      # print('あり')
      pass
    else:
      answer[d-2] += 1
      # print('なし')
      break
    d += 1

print(*answer)