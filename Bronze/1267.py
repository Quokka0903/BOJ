T = int(input())
Y, M = 0, 0
Call = list(map(int, input().split()))
for i in Call :
    Y += ((i // 30) + 1) * 10
    M += ((i // 60) + 1) * 15
if Y == M :
    print(f'Y M {Y}')
else :
    print(f'Y {Y}') if Y < M else print(f'M {M}')