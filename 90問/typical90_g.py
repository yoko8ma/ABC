import time

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]

a.sort()

for x in b:
  left_index = 0
  right_index = len(a) - 1
  mi = []

  while left_index <= right_index:
    middle_index = (left_index + right_index) // 2
    middle_value = a[middle_index]
    mi.append(abs(x-middle_value))

    if x < middle_value:
      right_index = middle_index - 1
      continue
    if x > middle_value:
      left_index = middle_index + 1
      continue
    break

  print(min(mi))