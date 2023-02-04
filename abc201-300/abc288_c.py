class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
 
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
 
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True
 
def kruskal(n, edges):
    uf = UnionFind(n)
    ans = 0
    for x, y in edges:
        if not uf.unite(x, y):
            ans += 1
    return ans

# 無向グラフのエッジリスト
# edges = [(0, 1), (1, 2), (2, 3), (3, 0), (2, 4)]

n, m = map(int, input().split())
a = [0]*m
b = [0]*m
edges = []

for i in range(m):
  a, b = map(int, input().split())
  edges.append((a-1, b-1))
# print(edges)
print(kruskal(n, edges)) # => 2
