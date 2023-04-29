import itertools

h, w = map(int, input().split())

mx = []

for _ in range(h):
    a = list(map(int, input().split()))
    mx.append(a)

# print(mx)
# l = ['h'] * (h-1) + ['w'] * (w-1)
# print(l)
s = []
e = (w+h-2)
for i in range(2 ** e):
    x = format(i, '0{}b'.format(e))
    # print(x)
    t = str(x)
    if t.count('0') != h-1:
       continue
    s.append(str(x))
# print(s)    
ans = 0

for x in s:
    # print(f'{x=}')
    v = []
    v.append(mx[0][0])
    i = 0
    j = 0
    flag = False

    for r in x:
        # print(f'{r=}')
        if r == '0':
          i += 1
        else:
          j += 1
        # print(i)
        # print(j)
        # print(v)
        if mx[i][j] in v:
          flag = True
          break
        else:
          v.append(mx[i][j])

    if flag == False:
       ans += 1

print(ans)