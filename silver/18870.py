import sys

input = sys.stdin.readline


T = int(input())
test = list(map(int, input().split()))
sets = sorted(set(test))
dic = {}
for i in sets:
    if i not in dic:
        dic[i] = 0

for w in dic:
    for v in dic:
        if w > v:
            dic[w] += 1

for i in test:
    print(dic[i], end=' ')