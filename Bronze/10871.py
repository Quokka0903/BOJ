N, X = map(int, input().split())
list = list(map(int, input().split()))
ans = ""
for i in range(N) : 
    if list[i] < X :
        ans += "{0} ".format(list[i])
print(ans)