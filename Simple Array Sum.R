
#December 2017 by Shuming Fang. 
#fangshuming519@gmail.com.
#https://github.com/FonzieTree
#https://www.hackerrank.com/challenges/simple-array-sum/problem
con=file('stdin',open='r')
open(con)
data=readLines(con,warn=F)
out=sum(as.numeric(strsplit(data[2],split=' ')[[1]]))
cat(out,'\n')
