N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]
print(N,S,M,T)
A = list(set(S+T))
print(A)
ms = []
for a in A:
  ms.append(S.count(a) - T.count(a))

mx = max(ms)
print(0 if mx < 0 else mx)
