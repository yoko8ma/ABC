N = int(input())
a1 = []
for i in range(N):
  a2 = []
  for j in range(i+1):
    if i == 0 or j == 0:
      a2.append(1)
    elif i==j:
      a2.append(1)
    else:
      a2.append(a1[i-1][j-1] + a1[i-1][j])
  print(*a2)
  a1.append(a2)
# print(a1)