G = 0
C = 2
P = 5

for x in [G, C, P]:
  for i in range(4):
    f = 0
    if x == G:
      f += P * 4-i
    elif x == C:
      f += C*(2+i)
    elif x == P:
      f += P*(2+i)
      f += C*4-i

    print(f)
