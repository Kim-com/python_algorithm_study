n, m, k= map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse = True)

# 수학적 풀이
num1 = data[0] # 1번째 큰 수
num2 = data[1] # 2번째 큰 수
sum = 0

count = m//(k+1)*k + m%(k+1)

sum = count*num1
sum += (m-count)*num2

print(sum)

# Greedy 풀이
# sum = 0
# m_cnt = 0
# k_cnt = 0
# while(1):
#   if(m_cnt >= m):
#     break
#   else:
#     if(k_cnt < k):
#       sum+=num1
#       k_cnt+=1
#       m_cnt+=1
#     else:
#       sum+=num2
#       k_cnt = 0
#       m_cnt+=1
#print(sum)