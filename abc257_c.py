
import bisect

n = int(input())
s = input()
w = list(map(int, input().split()))
sw = list(set(w))

ch = []
ad = []

for i, x in enumerate(list(s)):
  if x == '0':
    ch.append(w[i])
  else:
    ad.append(w[i])

ch.sort()
ad.sort()
print('こども', ch)
print('大人', ad)

wu = list(map(lambda x: x-0.1, sw))
wc = list(map(lambda x: x+0.1, sw))
print(w + wu + wc)
ans = 0

for x in w+wu+wc:
  print('x', x)
  h = 0

  i = bisect.bisect_left(ch, x)
  j = bisect.bisect_right(ad, x)

  print('こども正解', i+1)
  print('大人正解', )
  ans = max(ans, i+len(ad)-j)
  
print(ans)
