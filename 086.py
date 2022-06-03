'''
問題文
シカのAtCoDeerくんは二つの正整数 a,b を見つけました。 a と b の積が偶数か奇数か判定してください。

制約
1 ≤ a,b ≤ 10000
a,b は整数
入力
入力は以下の形式で標準入力から与えられる。

a b
出力
積が奇数なら Odd と、 偶数なら Even と出力せよ。
'''
a, b = map(int, input().split())
s = 'Odd' if a*b % 2 else 'Even'
print(s)
