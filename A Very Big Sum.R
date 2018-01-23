#https://www.hackerrank.com/challenges/a-very-big-sum/problem
options(scipen=200)
con=file('stdin',open='r')
open(con)
data=readLines(con,warn=F)
data=sum(as.numeric(strsplit(data[2],split=' ')[[1]]))
cat(data,'\n')
