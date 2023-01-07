import time

a = list(map(int, input().split()))

h = [a[0], a[1], a[2]]
w = [a[3], a[4], a[5]]
# m = [[0, 0, 0 ], [0, 0, 0 ], [0, 0, 0 ]]

# print(h, w, m)

ans = 0
ms = []
# im = max(h) - 1
# jm = max(h) - 1

for i1 in range(1, 29):
  for i2 in range(1, 29):
    for j1 in range(1, 29):
      for j2 in range(1, 29):
          m = [[0, 0, 0 ], [0, 0, 0 ], [0, 0, 0 ]]
          m[0][0] = i1
          m[0][1] = i2
          m[0][2] = h[0]-i1-i2
          if m[0][2] < 1:
            continue

          m[1][0] = j1
          m[1][1] = j2
          m[1][2] = h[1]-j1-j2  
          if m[1][2] < 1:
            continue

          m[2][0] = w[0] - m[0][0] - m[1][0]
          if m[2][0] < 1:
            continue
          m[2][1] = w[1] - m[0][1] - m[1][1]
          if m[2][1] < 1:
            continue
          
          m[2][2] = w[2] - m[0][2] - m[1][2]
          if m[2][2] < 1:
            continue

          s =  sum(sum(row) for row in m)
          if s != sum(h):
            continue

          ans += 1
          ms.append(m)

print(ans)
