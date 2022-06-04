N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]
# print(N, X, m)
# print(sum(m))
rest = X - sum(m)
# print(f'残り: {rest}')
# print(min(m))
q = rest//min(m)
print(N+q)