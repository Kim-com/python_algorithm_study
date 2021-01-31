#n = int(input())
#loute = list(map(str,input().split()))
n = 5
x,y = 1,1
loute = ['R','R','R','U','D','D']
print(loute)

# #책풀이
move_types = ['U','D','L','R']
dxy = [[-1,0],[+1,0],[0,-1],[0,+1]]

for move in loute :
  direction = move_types.index(move)
  nx = x + dxy[direction][0]
  ny = y + dxy[direction][1]

  if(nx<1 or nx>n or ny<1 or ny>n):
    continue
  else:
    x = nx
    y = ny

print(x,y)


#형준 풀이
# for dir in loute:
#   if(dir == 'U'):
#     x-=1
#   elif(dir == 'D'):
#     x+=1
#   elif(dir == 'R'):
#     y+=1
#   elif(dir == 'L'):
#     y-=1
#   else:
#     print("ERR")
#     break
#   if(x<1):
#     x = 1
#   elif(x>n):
#     x=n
#   elif(y<1):
#     y = 1
#   elif(y>n):
#     y=n
# print(x,y)