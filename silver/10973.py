N = int(input())
sunyeol = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    
    if sunyeol[i] < sunyeol[i-1]:

        x = i - 1
        y = i

        for j in range(N - 1, 0, -1):

            if sunyeol[j] < sunyeol[x]:
                sunyeol[j], sunyeol[x] = sunyeol[x], sunyeol[j]
                sunyeol = sunyeol[:i] + sorted(sunyeol[i:], reverse=True)
                print(*sunyeol)
                exit(0)
print(-1)