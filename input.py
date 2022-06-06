# a
s = input()
n = int(input())
f = float(input())

# a b
a, b = input().split()
x, y = map(int, input().split())
h, m = map(float, input().split())

# a b c ...
a = input().split()
a = list(map(int, input().split()))
a = list(map(float, input().split()))

# 3
# a
# b
# c
n = int(input())
a = [input() for _ in range(n)]
a = [int(input()) for _ in range(n)]
a = [float(input()) for _ in range(n)]

# 2
# a b c
# d e f
n, x = map(int, input().split())
a = [input().split() for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]
a = [list(map(float, input().split())) for _ in range(n)]

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
l_2d_ok = [[0] * w for i in range(h)]
