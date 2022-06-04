from re import I


s = input()
a = -1
z = 0

for i, x in enumerate(s):
  if x == 'A' and a == -1:
    a = i
  elif x == 'Z':
    z = i

  print(a, z)
print(z - a + 1)
