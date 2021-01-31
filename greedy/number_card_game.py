# 형준 풀이
# 입력값
# n = 3 
# m = 3
# data = [[3,1,2],[4,1,4],[2,2,2]]
# data = [[7,3,1,8],[3,3,3,4]]

# data = sorted(data, key = lambda x : min(x), 
# reverse = True)
# print(min(data[0]))

# 풀이1 : min 과 max 사용
n, m = map(int, input().split())
result = 0
for _ in range(n):
  data = list(map(int, input().split()))
  min_v = min(data)
  result = max(result,min_v)
print(result)
