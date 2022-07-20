T = int(input())
list_a = list(map(int, input().split()))
ans = []
for i in range(T) :
    ans.insert(list_a[i], (i + 1))

for i in range(T) :
    print(ans[T - i - 1], end = (" "))