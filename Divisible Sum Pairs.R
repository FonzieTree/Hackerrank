con=file('stdin','r')
open(con)
data=readLines(con)
data=as.numeric(unlist(strsplit(data,split=' ')))
k=data[2]
intg=data[3:(data[1]+2)]
mtx=as.matrix(combn(intg,2),,2)
cat(sum((mtx[1,]+mtx[2,])%%k==0),'\n')
