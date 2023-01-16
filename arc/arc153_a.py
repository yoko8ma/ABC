'''
123456789
aabcddefe
abcdef
123456
100000

11000000

abcdef
100001
aabcddefe
110000010

abcdef
100002
aabcddefe
110000020
'''

# a
n = int(input())

x = 100000 + n - 1
s = list(map(int, str(x)))
s = str(x)
# print(s)
ans = [s[0], s[0], s[1], s[2], s[3], s[3], s[4], s[5], s[4]]
# print(ans)
print(int(''.join(ans)))
