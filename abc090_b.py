A, B = map(int, input().split())
cnt = 0
for i in range(A, B+1):
  d = [int(x) for x in str(i)]
  if d == d[::-1]:
    cnt += 1
print(cnt)