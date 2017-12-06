con=file('stdin',open='r')
open(con)
data=readLines(con,warn=F)
data=as.numeric(data)
for(i in 1:data){
    out=paste0(strrep(" ",data-i),strrep("#",i),sep="")
    cat(out,"\n")
}
