n = int(input())
cp = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]
# print(n,cp,q,lr)

p1 = [0]*n
p2 = [0]*n

if cp[0][0] == 1:
  p1[0] = cp[0][1]
else:
  p2[0] = cp[0][1]

for i in range(1, n):
  # print(i, x)
  if cp[i][0] == 1:
    p1[i] = p1[i-1]+cp[i][1]
    p2[i] = p2[i-1]
  else:
    p1[i] = p1[i-1]
    p2[i] = p2[i-1]+cp[i][1]

# print(p1)
# print(p2)

for x in lr:
  s1 = p1[x[1]-1]-(0 if x[0] == 1 else p1[x[0]-2])
  s2 = p2[x[1]-1]-(0 if x[0] == 1 else p2[x[0]-2])
  print(s1, s2)  
  # s1 = 0
  # s2 = 0
  # for y in range(x[0]-1, x[1]):
  #   # print(cp[y])
  #   if cp[y][0] == 1:
  #     s1 += cp[y][1]
  #   else:
  #     s2 += cp[y][1]
  # print(s1, s2)
