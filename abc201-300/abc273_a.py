n = int(input())

def func(j):
  if j == 0:
    return 1
  else:
    return j * func(j - 1)

print(func(n))
