n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
#print(a)

x = 0
y = 0
now = 0
flag = True

for p in a:
  # print(p)
  t = p[0]  
  limit = t - now
  
  x_diff = abs(p[1] - x)
  y_diff = abs(p[2] - y)
  # print(f'現在時刻:{now}')
  # print(f'制限時間:{limit}')
  # print(f'現在地:{x},{y}')
  # print(f'目的地:{p[1]},{p[2]}')
  # print(f'移動時間:{x_diff},{y_diff}')
  x = p[1]
  y = p[2]
  limit -= x_diff
  limit -= y_diff
  # print(f'残り時間:{limit}')
  z = limit%2

  if limit < 0:
    flag = False
    break

  if z == 0:
    now = t
    continue
  else:
    flag = False
    break

if flag:
  print('Yes')
else:
  print('No')
