n, k = map(int, input().split())
s = ['']*n

for i in range(n):
  s[i] = input()

ans = s[:k]
ans.sort()

for x in ans:
  print(x)
