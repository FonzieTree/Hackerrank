import math
n=int(input().strip())
count=0
s=1.5
for i in range(n):
    temp=math.floor(s*3/2)
    count=count+temp
    s=temp
print(count)
