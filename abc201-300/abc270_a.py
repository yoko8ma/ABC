a, b = map(int, input().split())

aset = set()

if a == 1:
  aset.add(1)
elif a == 2:
  aset.add(2)
elif a == 3:
  aset.add(1)
  aset.add(2)
elif a == 4:
  aset.add(4)
elif a == 5:
  aset.add(1)
  aset.add(4)
elif a == 6:
  aset.add(2)
  aset.add(4)
elif a == 7:
  aset.add(1)
  aset.add(2)
  aset.add(4)

bset = set()

if b == 1:
  bset.add(1)
elif b == 2:
  bset.add(2)
elif b == 3:
  bset.add(1)
  bset.add(2)
elif b == 4:
  bset.add(4)
elif b == 5:
  bset.add(1)
  bset.add(4)
elif b == 6:
  bset.add(2)
  bset.add(4)
elif b == 7:
  bset.add(1)
  bset.add(2)
  bset.add(4)

ans = aset | bset
print(sum(ans))
