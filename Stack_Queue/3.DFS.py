def dfs(v, visited):
  
  visited[v] = True
  print(v, end = ' ')
  print(visited)
  for i in graph[v]:
    if(visited[i] == False):
      dfs(i,visited)

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False]*9

dfs(1,visited)
