
import itertools, math, copy
from re import U

n = int(input())
on = n
p = list(map(int, input().split()))
base = copy.copy(p)
base.sort()
h = 
# print(f'{p=}')

l = list(range(1, n+1))
print(f'{l=}')

p_list = []
for v in itertools.permutations(l, n):
  p_list.append(list(v))

# # p_list = list(itertools.permutations(l, n))
print(f'{p_list=}')

i = p_list.index(p)
print(*p_list[i-1])
