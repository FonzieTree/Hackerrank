# Enter your code here. Read input from STDIN. Print output to STDOUT
con=file('stdin','r')
data=readLines(con)
uchar=unique(strsplit(data,split='')[[1]])
ps=paste(uchar,uchar,sep='')
compute=function(){
for(i in 1:length(ps)){
    data=sub(pattern = ps[i], replacement = "", data)
    if(data==""){
        data="Empty String"
    }
    }
    return(data)
}
for(j in 1:length(strsplit(data,split='')[[1]])){
    data=compute()
}
cat(data,'\n')
