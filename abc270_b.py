x, y, z = map(int, input().split())

xa = abs(x)
ya = abs(y)
za = abs(z)
mi = min(xa, ya, za)

if xa == ya: # ゴールと壁が同じ距離
  print(xa)
elif ya == za: # 壁とハンマーが同じ距離
  if xa < ya: # ゴールが壁より近い
    print(xa)
  else:
    if xa * ya > 0: # ゴールと壁が同じ向き
      print(za*2+xa)
    else: # ゴールと壁が別の向き
      print(xa)
elif xa == za: # ゴールとハンマーが同じ距離
  if x * y < 0: #　ゴールと壁が別の向き
    print(xa)
  else: # ゴールと壁が同じ向き
    print(za*2+xa)
elif mi == xa:  # ゴールが一番近い
  print(xa)
elif mi == ya:  # 壁が一番近い
  if x * y < 0: #　ゴールと壁が別の向き
    print(xa)
  else: # ゴールと壁が同じ向き
    if y * z < 0: # 壁とハンマーが別の向き
      print(za*2+xa)
    else: # 壁とハンマーが同じ向き
      print(-1)
else: # ハンマーが一番近い
  if x * y < 0: #　ゴールと壁が別の向き
    print(xa)
  else: # ゴールと壁が同じ向き
    if y * z < 0: # 壁とハンマーが別の向き
      print(za*2+xa)
    else: # 壁とハンマーが同じ向き
      print(xa)
