package main

import "fmt"

func main() {
    var str string
    fmt.Scan(&str) // データを格納する変数のアドレスを指定
    fmt.Println(str)
}

// a
n = int(input())

// a b
a, b = map(int, input().split())

// a b c ...
a = list(map(int, input().split()))

// 3
// a
// b
// c
n = int(input())
a = [int(input()) for _ in range(n)]

// 2 3
// a b c
// d e f
n, x = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

// 数値を数字のリストへ
// 123 -> [1, 2, 3]
[int(x) for x in str(N)]
list(map(int, str(N)))

// 数字のリストを数値へ
// [1, 2, 3] -> 123
int(''.join([1, 2, 3]))

// 数字を1桁ずつ数字のリストへ
list(map(int, s))

// リストの偶数番目の要素
a = [0,1,2,3,4,5]
a[0::2]

// リストの奇数番目の要素
a = [0,1,2,3,4,5]
a[1::2]

// リストのrevers
a[::-1]

// 10進数->n進数
def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

// 2次元リストの初期化
l_2d_ok = [[0] * a for i in range(n)]

// 二分探索
import bisect
a=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
bisect.bisect(a,55) # => 5

// 尺取り法
l = 0
r = 0
while l < n:
    if r == n or '条件を満たさない':
	    #処理a
        l += 1    
    else:
	    # 処理b
        r += 1
    # 処理c
