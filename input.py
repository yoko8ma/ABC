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

# 文字列2次元配列
# N: 行数
A = [input().split() for _ in range(N)]
print(A)

# 整数2次元配列
A = [list(map(int, input().split())) for _ in range(N)]
print(A)

# 小数2次元配列
A = [list(map(float, input().split())) for _ in range(N)]
print(A)

# 数値を数字のリストへ
[int(x) for x in str(N)]
map(int, str(N))
