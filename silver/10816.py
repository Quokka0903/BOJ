import sys
input = sys.stdin.readline

N = int(input())
list_in = list(input().split())
M = int(input())
list_find = list(input().split())

list_cnt = {}
for i in list_in:
    if list_cnt.get(i) != None:
        list_cnt[i] += 1
    else :
        list_cnt[i] = 1

ans = []
for j in list_find:
    if list_cnt.get(j) != None:
        ans.append(list_cnt.get(j))
    else :
        ans.append(0)

print(*ans)