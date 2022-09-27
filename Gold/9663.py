import sys
input = sys.stdin.readline

cnt = 0

def queen(x, N):
    global cnt
    if x == N:
        cnt += 1
    else:
        for i in range(N):
            visited[x] = i
            for i in range(x):
                if visited[x] == visited[i] or abs(visited[x] - visited[i]) == abs(x - i):
                    break
            else:   
                queen(x + 1, N)

N = int(sys.stdin.readline())
visited = [0] * N
queen(0, N)
print(cnt)