con=file('stdin','r')
data=as.numeric(strsplit(readLines(con)[2],split=' ')[[1]])
high=0
low=0
if(length(data)>1){
for(i in 2:length(data)){
    if(data[i]>max(data[1:(i-1)])){
        high=high+1
    }
    if(data[i]<min(data[1:(i-1)])){
        low=low+1
    }
}
}
cat(c(high,low),'\n')
