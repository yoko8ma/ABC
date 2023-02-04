n, a, b = map(int, input().split())
s = input()

def min_cost(s: str, cost_a: int, cost_b: int) -> int:
    n = len(s)
    cost = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            cost += cost_b
    cost += (n // 2) * cost_a
    return cost

# 使用例
# s = "abcba"
# cost_a = 1
# cost_b = 2
print(min_cost(s, a, b))
