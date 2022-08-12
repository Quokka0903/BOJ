from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

chk_ps = {'(' : ')'}

for t in range(T):
    
    stack_self = deque()
    list_PS = input()

    for ps in list_PS:

        if stack_self and chk_ps.get(stack_self[-1]) == ps:
            stack_self.pop()
            continue
        if ps == '\n':
            continue
        stack_self.append(ps)
        
    
    if stack_self :
        print("NO")
    else :
        print("YES")