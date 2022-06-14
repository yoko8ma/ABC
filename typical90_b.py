n = int(input())

for i in range(2**n-1):
  s = format(i, f'0{n}b')
  # print(s)
  cnt = 0
  flag = True
  
  for j in range(n):
    if s[j] == '0':
      cnt += 1
    else:
      cnt -= 1
    
    if cnt < 0:
      flag = False
      break
  
  if flag and cnt==0:
    print(s.replace('0', '(').replace('1', ')'))