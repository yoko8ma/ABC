from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)
print(f'{graph=}')

for _ in range(n):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

print(f'{graph=}')

que = deque() # 到達した頂点
que.append(1)
S = {1} # 到達できる頂点

while que:
  # キューの先頭からpop
  v = que.popleft()
  print(f'{que=}')
  print(f'{v=}')

  # popした頂点と接続している頂点分ループ
  for i in graph[v]:
    print(f'{i=}')

    # 接続している頂点が辞書にない場合
    if not i in S:
      # キューの末尾へpush
      que.append(i)
      # 辞書へ追加
      S.add(i)
      print(f'{que=}')
      print(f'{S=}')

print(max(S))