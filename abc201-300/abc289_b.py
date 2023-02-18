n, m = map(int, input().split())

if m > 0:
  a = list(map(int, input().split()))
else:
  a = []

l = list(range(1, n+1))  # rangeオブジェクトから整数リスト（整数配列）を作成
# print(l)

st = []
ans = []

for i, x in enumerate(l):
  # print(f'{i=}')
  # print(f'{st=}')

  if (i+1) in a:
    # print('hit')
    st.append(x)
    # print(f'{st=}')
  else:
    ans.append(x)
    while len(st) > 0:
      # print('pop')
      ans.append(st.pop())
      # print(f'{st=}')

print(*ans)