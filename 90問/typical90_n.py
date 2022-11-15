n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

d = 0
for i in range(n):
  d += abs(a[i] - b[i])

print(d)
