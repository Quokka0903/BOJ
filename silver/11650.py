import sys
input = sys.stdin.readline

T = int(input())

ans =[]

for i in range(T) :
    ans.append(list(map(int,input().split())))

ans.sort(key = lambda x:(x[0], x[1]))

for unit in ans :

    print(f'{unit[0]} {unit[1]}')