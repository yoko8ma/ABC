n, m = map(int, input().split())
c = []

for _ in range(m):
  int(input())
  c.append(set(map(int, input().split())))

print(c)
