n = int(input())

def sieve(n):
    """エラトステネスの篩で n 以下の素数を生成する関数"""
    n = int(n ** (1/3))
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def count_patterns(n):
    """N 以下の正整数のうち、a<b<c なる素数 a,b,c を用いて a^2*b*c^2と表せるパターンの数を数える関数"""
    primes = sieve(n)
    # print(primes)
    count = 0

    for i in range(len(primes)-2):
        a = primes[i]

        for j in reversed(range(i + 2, len(primes))):
            c = primes[j]
            
            if a**2 * c**2 > n:
                break

            for k in range(i + 1, j):
                # print(i,j,k)
                b = primes[k]
                if a**2 * b * c**2 > n:
                    break
                # print(a,b,c)
                # print(a**2 * b * c**2)
                count += 1
    return count

# 使用例
print(count_patterns(n)) # 1
