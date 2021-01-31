n = int(input())

cnt = 0
for hour in range(n+1):
  if('3' in str(hour)):
    cnt+=60*60
  else:
    for minute in range(60):
      if('3' in str(minute)):
        cnt+=60
      else:
        for sec in range(60):
          if('3' in str(sec)):
            cnt+=1

print(cnt)