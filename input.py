# a
n = int(input())

# a b
a, b = map(int, input().split())

# a b c ...
a = list(map(int, input().split()))

# 3
# a
# b
# c
n = int(input())
a = [int(input()) for _ in range(n)]

# 2 3
# a b c
# d e f
n, x = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 数値を数字のリストへ
# 123 -> [1, 2, 3]
[int(x) for x in str(N)]
list(map(int, str(N)))

# 数字を1桁ずつ数字のリストへ
list(map(int, s))

# リストの偶数番目の要素
a = [0,1,2,3,4,5]
a[0::2]

# リストの奇数番目の要素
a = [0,1,2,3,4,5]
a[1::2]

# リストのrevers
a[::-1]

# 10進数->n進数
def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

# 2次元リストの初期化
l_2d_ok = [[0] * a for i in range(n)]
