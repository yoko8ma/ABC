#グラフオブジェクトを表すクラス
class Graph:
    #コンストラクター
    def __init__(self, edges, n):
        #は隣接リストにメモリを割り当てます
        self.adjList = [[] for _ in range(n)]
 
        #は有向グラフにエッジを追加します
        for (src, dest) in edges:
            #隣接リストのノードをsrcからdestに割り当てます
            self.adjList[src].append(dest)
 
 
# グラフの隣接リスト表現を印刷する#関数
def printGraph(graph):
    for src in range(len(graph.adjList)):
        #は、現在の頂点とそのすべての隣接する頂点を出力します
        for dest in graph.adjList[src]:
            print(f'({src} —> {dest}) ', end='')
        print()


n, x, y = map(int, input().split())
edges = []

for i in range(n-1):
  a, b = map(int, input().split())
  edges.append([a, b])

print(edges)

graph = Graph(edges, n)


# グラフの#印刷隣接リスト表現
printGraph(graph)