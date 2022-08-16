import sys

input = sys.stdin.readline

def cutting(a, n, dict):
    
    flag = True
    for i in range(1, n):
        if a[i - 1] != a[i]:
            flag = False
            break
        for j in range(1, n):
            if a[i][j - 1] != a[i][j]:
                flag = False
                break

    if flag == True:
        dict[a[0][0]] += 1
        return dict
    else :
        for i in range(3):
            for j in range(3):
                res = []
                for k in range(n // 3):
                    res.append(a[k + (n // 3 * i)][(n // 3 * j) : (n // 3 * j) + (n // 3)])
                cutting(res, n // 3, dict)


N = int(input())

sheet = [list(map(int, input().split())) for _ in range(N)]
res = {-1: 0, 0 : 0, 1 : 0}
cutting(sheet, N, res)

print(res[-1])
print(res[0])
print(res[1])