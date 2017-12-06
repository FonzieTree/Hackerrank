data=list(map(int,input().strip().split(' ')))
count=0
for i in range(data[0],data[1]+1):
    if (i-int(str(i)[::-1])) % data[2] ==0:
        count=count+1
print(count)
