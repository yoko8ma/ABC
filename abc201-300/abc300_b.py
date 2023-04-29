import numpy as np

h, w = map(int, input().split())

a = np.empty(0)
b = np.empty(0)
a = []
b = []

# print(a)

for i in range(h):
    s = input()
    m = list(s)
    a.append(m)

for i in range(h):
    s = input()
    m = list(s)
    b.append(m)

a = np.array(a)
b = np.array(b)
# print(a)
# print('---------------')
# print(b)
# print('---------------')
a = np.roll(a, 0, axis=0)

flag = False

for i in range(h+1):
  a = np.roll(a, 1, axis=0)

  for j in range(w+1):
    a = np.roll(a, 1, axis=1)
    if np.array_equal(a, b):
      flag = True

if flag:
   print('Yes')
else:
   print('No')
