from collections import deque
import sys

input = sys.stdin.readline
dict = {'(' : ')', '{' : '}', '[' : ']'}
pr = [')', '}', ']']

while True:
    stack = deque()
    str_in = input()
    if str_in == '.\n':
        break
    
    else :
        
        for i in str_in:
            if i == '.':
                break
            elif i not in dict and i not in pr:
                continue
            elif stack :
                if stack[-1] not in dict:
                    break
                elif i not in dict and dict[stack[-1]] == i:
                    stack.pop()
                    continue
            stack.append(i)

        if stack:
            print('no')
        else:
            print('yes')