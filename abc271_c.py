N = int(input())
a = set(map(int, input().split()))
read = 0
while N >= 0:
  read += 1
  N -= 1 if read in a else 2 # その巻を読むために使う本の冊数
print(read - 1) # 本が無くなったら、無くなる直前の冊数を出力
