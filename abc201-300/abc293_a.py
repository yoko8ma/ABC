s = input()
s = list(s)
for i in range(1, int(len(s)/2)+1):
    s[2*i-1-1], s[2*i-1] = s[2*i-1], s[2*i-1-1]

print(''.join(s))
