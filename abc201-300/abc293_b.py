n = int(input())
a = list(map(int, input().split()))

h = [False]*n

for i, x in enumerate(a):
    if h[i] == False:
        h[x-1] = True

cnt = 0
l = list()

for i, x in enumerate(h):
    if x == False:
        cnt += 1
        l.append(i+1)

print(cnt)
print(*l)