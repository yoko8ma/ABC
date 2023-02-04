n, x = map(int, input().split())

a = [0]*n
b = [0]*n
dic = {}

for i in range(n):
  a[i], b[i] = map(int, input().split())
  # dic[a] = b

# dic = sorted(dic.items(), reverse=True)
# l = list(dic)

# for i in range(n):
#   a = l[i][0]
#   b = l[i][1]
#   q, r = divmod(x, a)
#   # print(f'{q=}')
#   # print(f'{r=}')

#   if q <= b:
#     x -= a*q
#   else:
#     x -= a*b

# # print(x)

# if x == 0:
#   print('Yes')
# else:
#   print('No')


def can_pay_exactly(n, a, b, x):
    # dp[i+1][j] : using first i types of coins, can we pay j yen 
    dp = [[False] * (x + 1) for _ in range(n + 1)]

    # Initially, we can pay 0 yen with any number of any type of coin
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(n):
        for j in range(x + 1):
            # We can't pay j yen using i types of coins
            if j - a[i] < 0:
                dp[i + 1][j] = dp[i][j]
                continue
            # We can pay j yen using i types of coins
            if dp[i][j]:
                dp[i + 1][j] = True
                continue
            # We can pay j yen using i types of coins if we can pay j-a[i] yen using i types of coins and we have at least one coin of i-th type
            if dp[i][j - a[i]] and b[i] > 0:
                dp[i + 1][j] = True

    return dp[n][x]

# test
a = [1, 5, 10, 50, 100, 500]
b = [3, 2, 1, 3, 0, 2]
x = 620
print(f'{a=}')
print(f'{b=}')
print(f'{x=}')
print(can_pay_exactly(len(a), a, b, x))  # True
