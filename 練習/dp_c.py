n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# print(f"{a=}")

dp = [[0]*3 for _ in range(n)]
dp[0][0] = a[0][0]
dp[0][1] = a[0][1]
dp[0][2] = a[0][2]

# print(f"{dp=}\n")

for i in range(1, n):
  dp[i][0] = max(dp[i-1][1]+a[i][0], dp[i-1][2]+a[i][0])
  dp[i][1] = max(dp[i-1][0]+a[i][1], dp[i-1][2]+a[i][1])
  dp[i][2] = max(dp[i-1][0]+a[i][2], dp[i-1][1]+a[i][2])
  # print(f"{dp=}\n")

print(max(dp[-1]))
