N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [False] * N
stack = []

def res(depth, N, M):
    if depth == M:
        print(' '.join(map(str, stack)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            stack.append(L[i])
            res(depth+1, N, M)
            stack.pop()
            visited[i] = False

res(0, N, M)