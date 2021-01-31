n, k = map(int,input().split())

# 형준 풀이
# cnt = 0
# while(n!=1):
#   print(f"{cnt+1} : {n}")
#   if(n%k == 0):
#     n//=k
#   else:
#     n-=1
#   cnt+=1
# print(cnt)

#책 풀이
cnt = 0
while(n >= k):
  # (n==k로 나누어 떨어지는 수)가 될 떄까지 1씩 뺴기
  temp = (n//k)*k
  cnt += n - temp
  n = temp

  #나누기
  n //= k
  cnt += 1

cnt += (n-1)
print(cnt)