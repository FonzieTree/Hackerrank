#December 2017 by Shuming Fang. 
#fangshuming519@gmail.com.
#https://github.com/FonzieTree
#https://www.hackerrank.com/challenges/solve-me-first/problem
nums <- read.table("/dev/stdin", sep=" ");
nums <- as.list(as.data.frame(t(nums)))
write.table(as.numeric(nums[1])+as.numeric(nums[2]), sep = "", append=T, row.names = F, col.names = F)
