a, b, c, x, y = map(int, input().split())
ab = c*2
mp = max(a*x + b*y, ab*(x+y))

for i in range(max(x, y)+1):
  p = i*ab + max(0, x-i)*a + max(0, y-i)*b
  if p < mp:
    mp = p

print(mp)
