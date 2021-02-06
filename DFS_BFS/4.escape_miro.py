from collections import deque

def data_iuput():
  n, m = map(int, input().split())
  data = list()
  for i in range(n):
    data.append(list(map(int,input())))
  return n,m,data

drs = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs():
  que = deque([(0,0)])
  while(que):
    x,y = que.popleft()
    for dx,dy in drs:
      if(x+dx < 0 or y+dy < 0 or x+dx >=n or y+dy >=m):
        continue
      elif(data[x+dx][y+dy] == 1):
        data[x+dx][y+dy] = data[x][y] + 1
        que.append((x+dx,y+dy))
  return data[n-1][m-1]

if __name__ == '__main__':
  n,m,data= data_iuput()
  print(bfs())