s = input()
t = []

for i, x in enumerate(s):
  if i%2 == 0:
    t.append(x)
    # print(x)

print(''.join(t))