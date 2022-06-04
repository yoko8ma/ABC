N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
d = 1000
for i, x in enumerate(H):
  at = T - x * 0.006
  # print(at)
  a = abs(A - at)
  # print(a)
  if a < d:
    p = i
    d = a

print(p+1)