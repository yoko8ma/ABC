def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

n, k = map(int, input().split())

for i in range(k):
  n = int(str(n), 8) # 8->10
  n = base10int(n, 9) # 10->9
  n = n.replace('8', '5')

print(n)
