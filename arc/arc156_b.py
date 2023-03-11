MOD = 998244353

def mex_set(S):
    return set(range(len(S)+1)) - set(S)

N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    dp[i][0] = 1
    for j in range(1, K+1):
        if len(mex_set(A[:i-1])) == 0:
            dp[i][j] = dp[i-1][j]
        else:
            coeff = len(mex_set(A[:i-1]).intersection(set([j-1])))
            inv = pow(len(mex_set(A[:i-1])), MOD-2, MOD) if len(mex_set(A[:i-1])) != 0 else 0
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1] * coeff * inv) % MOD

print(dp[N][K])
