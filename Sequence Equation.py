num=int(input().strip())
data=list(map(int,input().strip().split(' ')))
for i in range(num):
    temp=data.index(i+1)+1
    print(data.index(temp)+1)
