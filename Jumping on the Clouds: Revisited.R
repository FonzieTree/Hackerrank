# Enter your code here. Read input from STDIN. Print output to STDOUT
f=file('stdin','r')
open(f)
data=readLines(f)
n=as.numeric(strsplit(data[1],split=' ')[[1]][1])
k=as.numeric(strsplit(data[1],split=' ')[[1]][2])
gg=as.numeric(strsplit(data[2],split=' ')[[1]])
index=seq(1,n,by=k)
output=sum(gg[index]==1)*2+length(index)
output=100-output
cat(output,'\n')
