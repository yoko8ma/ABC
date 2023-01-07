n = int(input())
s = input()

ans = []
sf = False

for c in s:
  # print(c)
  
  if c == '"':
    if not sf:
      sf = True
    else:
      sf = False
    ans.append(c)
  elif c ==  ",":
    if sf:
      ans.append(",")
    else:
      ans.append(".")
  else:
    ans.append(c)

print("".join(ans))
