from collections import deque
import sys

T = int(sys.stdin.readline())

test = deque()

for t in range(T) :
    order = list(sys.stdin.readline().split())

    if order[0] == 'push_back' :
        test.append(order[1])

    elif order[0] == 'push_front' :
        test.appendleft(order[1])

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

    elif order[0] == 'size' :
        print(len(test))

    elif order[0] == 'empty' :
        if test :
            print(0)
        else :
            print(1)

    elif order[0] == 'pop_front' :
        if test :
            print(test.popleft())
        else :
            print(-1)

    elif order[0] == 'pop_back' :
        if test :
            print(test.pop())
        else :
            print(-1)

    elif order == 'front' :
        if test :
            print(test[0])
        else :
            print(-1)