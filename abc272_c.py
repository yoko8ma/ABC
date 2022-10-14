n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)

es = []
os = []
ans = []

flag = False

for x in a:
  if x % 2 == 0: # 偶数
    es.append(x)
    if len(es) == 2:
      ans.append(sum(es))
      flag = True
  else: # 奇数
    os.append(x)
    if len(os) == 2:
      ans.append(sum(os))
      flag = True

if flag:
  print(max(ans))
else:
  print(-1)
