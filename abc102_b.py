N = int(input())
A = list(map(int, input().split()))
# print(A)
min = 1000000000
max = 0
for i in A:
  if i < min:
    min = i
  if i > max:
    max = i
print(max - min)