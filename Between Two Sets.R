con=file('stdin',open='r')
open(con)
data=readLines(con,warn=F)
data1=as.numeric(unlist(strsplit(data[1],split=' ')))
data2=as.numeric(unlist(strsplit(data[2],split=' ')))
data3=as.numeric(unlist(strsplit(data[3],split=' ')))
prepare=rep(max(data2):min(data3))
m1=prepare%*%t(1/data2)%%1==0
m2=t(data3%*%t(1/prepare))%%1==0
out=sum(rowSums(m1)==dim(m1)[2]&rowSums(m2)==dim(m2)[2])
cat(out,'\n')
