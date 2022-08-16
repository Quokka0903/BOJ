import sys

input = sys.stdin.readline

T = int(input())

S = set()

for t in range(T):
    orderlist = list(input().split())

    if orderlist[0] == 'add':
        S.add(orderlist[1])
    
    elif orderlist[0] == 'remove':
        S.discard(orderlist[1])

    elif orderlist[0] == 'check':
        if orderlist[1] in S:
            print(1)
        else:
            print(0)
    
    elif orderlist[0] == 'toggle':
        if orderlist[1] in S:
            S.discard(orderlist[1])
        else :
            S.add(orderlist[1])
    
    elif orderlist[0] == 'all':
        S = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}
    
    elif orderlist[0] == 'empty':
        S = set()
