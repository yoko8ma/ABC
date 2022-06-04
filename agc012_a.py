N = int(input())
A = list(map(int, input().split()))
A.sort()
print(A)
p = 0
for i, a in enumerate(A):
  if i%2 == 0:
    p += a

print(p)

A = A[::-1]
print(A)
A = A[N:]
print(A)
A = A[:N]
print(A)
print(sum(A))