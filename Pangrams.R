# Enter your code here. Read input from STDIN. Print output to STDOUT
con=file('stdin','r')
open(con)
data=readLines(con)
dict=c('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
sti=strsplit(data,split='')[[1]]
sti=unique(sti)
out="not pangram"
if(length(unique(tolower(sti[which(sti%in%dict)])))==26){
    out="pangram"
}
cat(out,'\n')
