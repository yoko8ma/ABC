N, K = map(int, input().split())
A = list(map(int, input().split()))
print(N, K, A)
A = sorted(A)[::-1]
print(A)
print(A[:3])
print(sum(A[:K]))
