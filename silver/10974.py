n = int(input())
permut = []

def dfs():
    if len(permut) == n:
        print(*permut)
        return
    for i in range(1, n + 1):
        if i not in permut:
            permut.append(i)
            dfs()
            permut.pop()

dfs()