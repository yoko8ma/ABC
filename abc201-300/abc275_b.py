a, b, c, d, e, f = map(int, input().split())
m = ((a*b*c)-(d*e*f)) % 998244353
print(m)