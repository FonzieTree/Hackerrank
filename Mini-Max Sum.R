con=file('stdin',open='r')
open(con)
data=readLines(con,warn=F)
data=as.numeric(unlist(strsplit(data,split=' ')))
total=sum(data)
dmin=min(data)
dmax=max(data)
out1=total-dmax
out2=total-dmin
out=c(out1,out2)
cat(out,'\n'
