from collections import deque

drt = [(-1,0),(0,1),(1,0),(0,-1)]

def input_data():
  n, m = map(int, input().split())
  data = list()
  for i in range(n):
    data.append(list(map(int,input())))
  return n, m, data

#Sol
def dfs_sol(x, y, data):
  if(x<0 or y<0 or x>=n or y>=m):
    return False
  if(data[x][y]==0):
    data[x][y] = 1
    dfs_sol(x-1,y,data)
    dfs_sol(x+1,y,data)
    dfs_sol(x,y+1,data)
    dfs_sol(x,y-1,data)
    return True
  return False

#형준
def dfs(x, y, data):
  data[x][y] = 1
  for dx,dy in drt:
    if(x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= n):
      continue
    elif(data[x+dx][y+dy] == 0):
      dfs(x+dx, y+dy, data)

#형준
def bfs(x,y, data):
  que = deque([(x,y)])
  while(que):
    temp = que.popleft()
    print(temp, type(temp))
    x, y = temp
    for dx,dy in drt:
      if(x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= n):
        continue
      elif(data[x+dx][y+dy] == 0):
        data[x+dx][y+dy] = 1
        que.append((x+dx, y+dy))

if __name__ in "__main__" :
  n, m, data = input_data()
  cnt = 0

  for x in range(n):
    for y in range(m):
      #형준
      # if(data[x][y] == 0):
      #   # dfs(x, y, data)
      #   bfs(x, y, data)
      #   cnt+=1

      #sol
      if(dfs_sol(x,y,data) == True):
        cnt+=1

  print(cnt)