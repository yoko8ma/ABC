N = int(input())
L = list(map(int, input().split()))
print(N, L)
cnt = 0

for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
      e = [L[i], L[j], L[k]]
      print(e)
      if L[i]==L[j] or L[j]==L[k] or L[i]==L[k]:
        continue
      e1 = max(e)
      e.remove(e1)
      print(e1)
      print(e)
      if e1 < sum(e):
        cnt += 1
      print(cnt)
print(cnt)
