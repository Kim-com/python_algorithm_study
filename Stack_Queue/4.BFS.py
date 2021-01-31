from collections import deque




def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  while(queue):
    cur_node = queue.popleft()
    print(cur_node, end = ' ')
    for next_node in graph[cur_node]:
      if(not visited[next_node]):
        queue.append(next_node)
        visited[next_node] = True

if __name__ == '__main__':
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
  visited = [False]*len(graph)
  bfs(graph,1,visited)
