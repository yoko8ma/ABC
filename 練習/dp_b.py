N, K = map(int, input().split())
h = list(map(int, input().split()))

# DP配列を用意
# dp[i]にはi番目の足場にたどり着くために必要な最低コストを入れる
dp = [0] * N

# 初期条件
dp[0] = 0

# DP
for i in range(1, N):
  a = []

  for j in range(1, K+1):
    if i-j < 0:
      break

    a.append(dp[i-j] + abs(h[i]-h[i-j]))
  
  dp[i] = min(a)
  print(f"{dp=}\n")

# dp配列の末尾がN番目の足場へ行くためのコスト
print(dp[-1])