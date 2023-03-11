def min_flips(s):
    n = len(s)
    # 偶数の場合、表向きになっているコインの数と裏向きになっているコインの数が等しければ、全てを裏向きにできる
    if n % 2 == 0:
        if s.count('1') % 2 == 0:
            return s.count('1') // 2
        else:
            return -1
    else:
        ones = s.count('1')
        # 000
        # 001
        # 010
        # 011
        # 100
        # 101
        # 110
        # 111
        if ones % 2 == 1:
            return -1
        else:
          flips = 0
          for i in range(1, n):
              if s[i-1:i+1] == '00':
                  flips += 1
          
          # Check if all coins are tails
          if s.count('1') == n:
              return flips
          else:
              return -1

t = int(input())

for i in range(t):
  n = int(input())
  s = input()
  ans = min_flips(s)
  print(ans)
