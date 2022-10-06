x, y, z = map(int, input().split())

xa = abs(x)
ya = abs(y)
za = abs(z)
# mi = min(xa, ya, za)
mi = min(x, y, z)

if mi == x: # ゴールが一番小さい
  if y < z: # ゴール　壁　ハンマー
    if x > 0:
      print(xa)
    elif y > 0:
      print(xa)
    elif z > 0:
      print(za*2+xa)
    else:
      print(xa)  
  else: # ゴール　ハンマー　壁
    if x > 0:
      print(xa)
    elif z > 0:
      print(xa)
    elif y > 0:
      print(xa)
    else:
      print(-1)
elif mi == y: # 壁が一番小さい
  if x < z: # 壁　ゴール　ハンマー
    if y > 0:
      print(-1)
    elif x > 0:
      print(xa)
    elif z > 0:
      print(xa)
    else:
      print(xa)
  else:  # 壁　ハンマー　ゴール
    if y > 0:
      print(-1)
    elif z > 0:
      print(xa)
    elif x > 0:
      print(xa)
    else:
      print(xa)
else: # ハンマーが一番小さい
  if x < y: # ハンマー　ゴール　壁
    if z > 0:
      print(xa)
    elif x > 0:
      print(xa)
    elif y > 0:
      print(xa)
    else:
      print(-1)
  else: # ハンマー　壁　ゴール
    if z > 0:
      print(xa)
    elif y > 0:
      print(za*2+xa)
    elif x > 0:
      print(xa)
    else:
      print(xa)
