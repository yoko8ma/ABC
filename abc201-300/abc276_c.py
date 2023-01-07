import itertools, math, copy
from re import U

n = int(input())
on = n
p = list(map(int, input().split()))
base = copy.copy(p)
base.sort()
# print(f'{p=}')

l = list(range(1, n+1))
# # print(f'{l=}')

# p_list = []
# for v in itertools.permutations(l, n):
#   p_list.append(list(v))

# # # p_list = list(itertools.permutations(l, n))
# print(f'{p_list=}')

# i = p_list.index(p)
# print(*p_list[i-1])

i = 0

for x in p:
  # 1数字での範囲
  u = int(math.factorial(n) / n)
  # print(f'{u=}')
  n -= 1

  # 数の最初のインデックス
  # print(f'{x=}')
  idx = base.index(x)
  # print(f'{idx=}')
  c = (idx)*u
  # print(f'{c=}')
  i += c
  # print(f'{i=}')
  # print(f'{p_list[i]=}')
  base.remove(x)

i -= 1
# print(f'{i=}')
# print()
n = on
base = copy.copy(p)
base.sort()
ans = []

while True:
  # 1数字での範囲
  u = int(math.factorial(n) / n)
  # print(f'{u=}')
  n -= 1

  q = i // u
  i = i % u
  # print(f'{q=}')
  ans.append(base[q])
  base.remove(base[q])
  
  if base == []:
    break

print(*ans)
