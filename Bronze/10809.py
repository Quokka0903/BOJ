T = int(input())
min = 1000000
max = -1000000
idx = list(map(int, input().split()))
for i in range(T) :
    if min > idx[i] :
        min = idx[i]
    if max < idx[i] :
        max = idx[i]
print("{0} {1}".format(min, max))