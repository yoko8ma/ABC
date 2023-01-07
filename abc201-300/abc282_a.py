k = int(input())

t =[]

st = ord("A")

for i in range(k):
  t.append(chr(st + i))

ans = ''.join(t)
print(ans)
