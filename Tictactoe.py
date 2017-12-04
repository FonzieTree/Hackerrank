# problem from https://www.hackerrank.com/challenges/tic-tac-toe
'''
R code part
library(ReinforcementLearning)
data=tictactoe
control <- list(alpha = 0.1, gamma = 0.1, epsilon = 0.1)
model <- ReinforcementLearning(data, s = "State", a = "Action", r = "Reward",
s_new = "NextState", control = control)
write.table(model$Policy,'policy.txt')
'''
#######making format########
import json
dic1 = dict()
dic2 = dict()
with open("D:\\hero\\tictac.txt") as f:
    for lines in f:
        line = lines.strip().split('"')
		state = list(line[1])
        label = line[3][1]
		for i in range(len(state)):
			if state[i] == 'B':
                state[i] = 'O'
            elif state[i] == '.':
                state[i] = '_'				
		label = int(label) - 1
        state2 = state
        for i in range(len(state2)):
            if state2[i] == 'X':
                state2[i] = 'O'
            elif state2[i] == 'O':
                state2[i] = 'X'			
		state = ''.join(state)
        state2 = ''.join(state2)
		dic1[state] = label
        dic2[state2] = label
with open('dic1.json','w') as fp:
    json.dump(dic1,fp)
with open('dic2.json','w') as fp:
    json.dump(dic2,fp)

#######predicting##########
dic1 = ...
dic2 = ...
char = input()
string = [input() for i in range(3)]
string = ''.join(string)
if string == 'X':
    out = dic1[string]
elif string == 'O':
    out = dic2[string]
if out == '0':
    print('0 0')
elif out == '1':
    print('0 1')
elif out == '2':
    print('0 2')
elif out == '3':
    print('1 0')
elif out == '4':
    print('1 1')
elif out == '5':
    print('1 2')
elif out == '6':
    print('2 0')
elif out == '7':
    print('2 1')
elif out == '8':
    print('2 2')
