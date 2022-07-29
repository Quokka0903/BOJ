T = int(input())
for _ in range(T) :
    N, list_a = list((input(). split()))
    ans = ''
    for i in range(len(list_a)) :
        for _ in range(int(N)) :
            ans += list_a[i]
    print(ans)