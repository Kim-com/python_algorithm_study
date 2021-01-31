# def recursive_function(i):
#   if i == 100:
#     return
#   print(i, '번째 재귀 함수에서 ',i+1,'번째 재귀 함수를 호출합니다.')
#   recursive_function(i+1)
#   print(i,'번재 재귀 함수를 종료합니다.')

# recursive_function(0)

def factorial(n):
  if(n<=1):
    return 1
  return n*factorial(n-1)
fact = factorial(10)
print(fact)