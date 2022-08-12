from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

test = deque()

for t in range(T) :
    order = list(input().split())

    if order[0] == 'push' :
        test.append(order[1])
    
    elif order[0] == 'front' :
        if test :
            print(test[0])
        else :
            print(-1)

    elif order[0] == 'back' :
        if test :
            print(test[-1])
        else :
            print(-1)

    elif order[0] == 'pop' :
        if test :
            print(test.popleft())
        else :
            print(-1)
    
    elif order[0] == 'size' :
        print(len(test))

    elif order[0] == 'empty' :
        if test :
            print(0)
        else :
            print(1)