N = int(input())
h = list(map(int, input().split()))

# DP配列を用意
# dp[i]にはi番目の足場にたどり着くために必要な最低コストを入れる
dp = [0] * N

# 初期条件
dp[0] = 0
dp[1] = abs(h[1] - h[0])

# DP
for i in range(2, N):
  # i を現在いる足場と考える
  # i 番目の足場へ行く方法としてi-1番目からのジャンプとi-2番目からのジャンプがある
  # 2通りの行き方のうちコストの少ない方をdp[i]とする
  dp[i] = min(dp[i-2]+abs(h[i]-h[i-2]), dp[i-1]+abs(h[i]-h[i-1]))

# dp配列の末尾がN番目の足場へ行くためのコスト
print(dp[-1])