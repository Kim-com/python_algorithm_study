x,y = list(input())
x = ord(x)-ord('a')+1
y = int(y)
print(x,y)

dx = [-1,-1,+1,+1,-2,+2,-2,+2]
dy = [-2,+2,-2,+2,-1,-1,+1,+1]
cnt=0

for px,py in zip(dx,dy):
  nx = x+px
  ny = y+py
  if(nx<1 or nx>8 or ny<1 or ny>8):
    continue
  else:
    cnt+=1
  print(cnt)