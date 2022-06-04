N, L = map(int, input().split())
S = [input() for _ in range(N)]
print(N, L, S)
S.sort()
print(S)
print(''.join(S))
