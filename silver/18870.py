import sys

input = sys.stdin.readline


T = int(input())
test = list(map(int, input().split()))
sets = sorted(set(test))
dic = {}
i = 0
for w in sets:
    dic[w] = i
    i += 1

for i in test:
    print(dic[i], end=' ')