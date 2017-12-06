con=file('stdin',open='r')
open(con)
data=readLines(con,warn=F)
data=as.numeric(unlist(strsplit(data,split=' '))[-1])
num=length(data)
for(i in 1:num){
    out=data[i]
    if(data[i]%%10>7 & data[i]>37){
        out=round(data[i]/10)*10
    }
    if(data[i]%%10>2 & data[i]%%10<5 & data[i]>37){
        out=as.numeric(paste(round(data[i]/10),5,sep=""))
    }   
    cat(out,'\n')
}
