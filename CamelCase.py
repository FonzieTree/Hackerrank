# Enter your code here. Read input from STDIN. Print output to STDOUT
con=file('stdin','r')
open(con)
data=readLines(con)
dict=c('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
sti=strsplit(data,split='')[[1]]
cat(sum(sti%in%dict)+1,'\n')
