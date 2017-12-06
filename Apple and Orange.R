con=file('stdin','r')
data=readLines(con)
sam=as.numeric(strsplit(data[1],split=' ')[[1]])

tree=as.numeric(strsplit(data[2],split=' ')[[1]])

apple=as.numeric(strsplit(data[4],split=' ')[[1]])

orange=as.numeric(strsplit(data[5],split=' ')[[1]])

out1=sum(((tree[1]+apple)>=sam[1])&((tree[1]+apple)<=sam[2]))
out2=sum(((tree[2]+orange)>=sam[1])&((tree[2]+orange)<=sam[2]))
cat(out1,'\n')
cat(out2,'\n')
