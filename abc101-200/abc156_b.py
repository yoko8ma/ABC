def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

N, K = map(int, input().split())
a = base_n(N, K)
print(a)
a = list(map(int, str(a)))
print(a)
print(len(a))