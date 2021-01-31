# n, m = list(map(int,input().split()))
# x, y, cur_dir = list(map(int,input().split()))

# map_data = list()
# for i in range(n):
#   map_data.append(list(map(int,input().split())))

n = 3
m = 3
x = 1
y = 1
cur_dir = 0
map_data = [[1,1,1],[1,0,0],[1,1,0]]


#북, 동, 남, 서
dx = [-1,0,+1,0]
dy = [0,+1,0,-1]

count = 0
turn_time = 0
def turn_left(cur_dir):
  cur_dir-=1
  if(cur_dir < 0):
    cur_dir = 3
  return cur_dir

def print_map(x, y, direction):
  print('=============')
  for i in range(n):
    for j in range(m):
      if(i==x and j==y):
        print('*', end = '  ')
      elif(i == x + dx[direction] and j == y + dy[direction]):
        print('+', end = "  ")
      else:
        print(map_data[i][j], end = '  ')
    print('')

  
while(True):
  map_data[x][y] = -1
  print_map(x, y, cur_dir)
  
  turn_time += 1
  if(turn_time > 4):
    x = x - dx[cur_dir]
    y = y - dy[cur_dir]
    if(map_data[x][y] == -1):
      turn_time = 0
    elif(map_data[x][y] == 1):
      break
    else:
      input()
  
  cur_dir = turn_left(cur_dir)

  nx = x + dx[cur_dir]
  ny = y + dy[cur_dir]
  
  if(nx<0 or nx>=n or ny<0 or ny>=m):
    continue
  elif(map_data[nx][ny] == 0):
    x, y = nx, ny
    count+=1
    turn_time = 0
print(count+1)