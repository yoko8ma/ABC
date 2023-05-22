n = int(input())
s = input()
s = list(s)

flag = False
ans = 'out'

for x in s:
    if x =='|':
        if flag == False:
          flag = True
        else:
           flag = False
    elif x == '*':
       if flag:
          ans = 'in'
          break

print(ans)
