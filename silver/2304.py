T = int(input())
list_a = []
for i in range(T) :
    list_a.append(list(map(int, input().split())))
list_a = (sorted(list_a)) # 크기 순서로 정렬
max, idx, endidx = 0, 0, 0
for i in range(T) :
    if max < (list_a[i][1]) :
        max = list_a[i][1] # 최댓값 인덱스와 넓이 (앞에서)
        idx = list_a[i][0]
endidx = list_a[T-1][0]

list_b = [0] * (endidx + 1)
for x, y in list_a :
    list_b[x] = y

ans = 0
compare = 0
for i in range(idx + 1) :
    if compare < list_b[i] :
        compare = list_b[i]
    ans += compare

compare = 0
for i in range(endidx, idx, -1) :
    if compare < list_b[i] :
        compare = list_b[i]
    ans += compare

print(ans)