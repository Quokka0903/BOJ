import collections
import sys
input = sys.stdin.readline

for t in range(int(input())):
    p = input()
    n = int(input())
    plist = collections.deque(input().lstrip('[').rstrip(']\n').split(','))

    if not n:
        plist.pop()

    dir = 1
    flag = 1
    for unit in p:
        if unit == 'R':
            dir *= -1
        elif unit == 'D':
            if plist:
                if dir == 1:
                    plist.popleft()
                elif dir == -1:
                    plist.pop()
            else:
                print('error')
                flag = 0
                break
    
        #print(plist)
    
    if plist:
        if dir == 1:
            plist = list(plist)
        else:
            plist = list(plist)[::-1]

        print('[' + ",".join(plist) + ']')

    else:
        if flag:
            print('[' + ']')