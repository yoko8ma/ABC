n = int(input())
s = [input() for _ in range(n)]

r = []
for x in s:
  r.append(list(map(int, x)))

t = []
now = 0

for i in range(n):
  h = r[i][0] # 先頭の数字
  print(f'当て数{h}')
  hi = []

  # リールの全探索
  for j,v in enumerate(r):
    if i == j: # 自身は探索しない
      print('self')
      continue

    pos = v.index(h)
    print(f'位置 {pos}')
    if pos <= now:
      pos += 10 + now
      now += 10
    hi.append(pos)
  
  t.append(max(hi))

print(t)
print(min(t))
