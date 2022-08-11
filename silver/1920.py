N = int(input())
list_num = set(map(int, input().split()))
M = int(input())
list_comp = list(map(int, input().split()))

ans = list_num & set(list_comp)
for res in list_comp :
    if res in ans :
        print(1)
    else :
        print(0)