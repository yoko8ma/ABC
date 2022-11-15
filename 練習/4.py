N = int(input())

sq = []
a = 1

for i in range(1, N+1):
    sq.append(i*i)

# print(sq)
cnt = 0

for s in sq:
  print(s)

  for i in range(1, s+1):
    print(i)
    print(f'あまり{s%i}')
    if s%i == 0:
      cnt += 1

# for i in range(1, N+1):
#   for j in range(1, N+1):
#       # print(i,j)
#       # print(i*j)
#       if i*j in sq:
#         cnt += 1
print(cnt)