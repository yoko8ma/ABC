n, a, b = map(int, input().split())
s = [x for x in range(1, n+1) if a <= sum(map(int, str(x))) <= b]
print(sum(s))

c = 0
for i in range(1, n+1):
#  print(i)
  s = i//100 + i//10 + i%10
#  print(s)
  num = [int(x) for x in str(i)]
#  print(num)
  m = map(int, str(i))
#  print(sum(num))

  if a <= sum(num) <= b:
    c +=i
