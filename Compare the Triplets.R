#December 2017 by Shuming Fang. 
#fangshuming519@gmail.com.
#https://github.com/FonzieTree
#https://www.hackerrank.com/challenges/compare-the-triplets/problem
con=file('stdin',open='r')
open(con)
data=read.table(con)
result=data[1,]-data[2,]
out1=sum(result>0)
out2=sum(result<0)
cat(c(out1,out2),'\n')
