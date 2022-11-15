import collections

N, K = map(int, input().split())
A = list(map(int, input().split()))
print(N,K,A)
c = collections.Counter(A)
print(c)
print(c.values())
l = list(c.values())
l.sort()
print(l)
print(l[-K:])
print(sum(l) - sum(l[-K:]))
