con=file('stdin',open='r')
open(con)
data=readLines(con,warn=F)
data1=as.numeric(unlist(strsplit(data[1],split=' ')))
data2=as.numeric(unlist(strsplit(data[2],split=' ')))
data3=as.numeric(unlist(strsplit(data[3],split=' ')))
out=data2[t(matrix(rep(1:data3[2]),data3[2],data1-data3[2]+1))+t(matrix(rep(0:(data1-data3[2]),each=data3[2]),data3[2]))]
cat(sum(rowSums(matrix(out,,data3[2]))==data3[1]),'\n')
