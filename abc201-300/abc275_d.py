import math
import time

def func2(v):
  # time.sleep(1)
  # print(f'{v=}')
  # print(f'{v in d=}')

  m2 = math.floor(v/2)
  m3 = math.floor(v/3)

  if v in d:
    # print('hit')
    return d[v]

  if m2 in d:
    # print('hit2')
    d[v] = d[m2] + func2(m3)
    # print(f'{d=}')
    return d[m2] + func2(m3) 

  if m3 in d:
    # print('hit3')
    d[v] = func2(m2) + d[m3]
    # print(f'{d=}')
    return func2(m2) + d[m3]

  # if v == 0:
  #   return 1

  return func2(m2) + func2(m3)

# def func3(v):
#   if v == 0:
#     return 1

#   return func2(math.floor(v/2)) + func2(math.floor(v/3))

n = int(input())

d = {0: 1}

# ans = func2(n) + func3(n)
ans = func2(n)

# a = []

# for i in range(1,n+1):
#   print(f'{i=}')
#   a.append(math.floor(i/2))
#   a.append(math.floor(i/3))

# print(a)

print(ans)
