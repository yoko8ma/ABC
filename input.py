# 文字列
S = input()
print(S)

# 整数
N = int(input())
print(N)

# 小数
F = float(input())
print(F)

# 複数文字列
A, B = input().split()
print(A, B)

# 複数整数
X, Y = map(int, input().split())
print(X, Y)

# 複数小数
H, M = map(float, input().split())
print(H, M)

# 文字列配列
A = input().split()
print(A)

# 整数配列
A = list(map(int, input().split()))
print(A)

# 小数配列
A= list(map(float, input().split()))
print(A)

# 1行に複数の整数
# 4
# 5 6 8 10
N = int(input())
A = list(map(int, input().split()))

# 複数行の整数
# 2
# 5
# 1
N = int(input())
A = [int(input()) for _ in range(N)]

# 文字列2次元配列
# N: 行数
A = [input().split() for _ in range(N)]
print(A)

# 整数2次元配列
H, W = map(int, input().split())
A = [int(input()) for _ in range(H)]

# 整数2次元配列
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
print(A)

# 小数2次元配列
A = [list(map(float, input().split())) for _ in range(N)]
print(A)

# 複数行数値
N = int(input())
A = [int(input()) for _ in range(N)]

# 数値を数字のリストへ
[int(x) for x in str(N)]
map(int, str(N))

# リストの偶数番目の要素
a = [0,1,2,3,4,5]
a[0::2]

# リストの奇数番目の要素
a = [0,1,2,3,4,5]
a[1::2]