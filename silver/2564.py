def wuichi (d, M, N):
    if d[0] == 1:
        return 0, d[1]
    elif d[0] == 2:
        return N, d[1]
    elif d[0] == 3:
        return d[1], 0
    else :
        return d[1], M


M, N = map(int, input().split())
T = int(input())

sangjeom = []
for t in range(T + 1):
    sangjeom.append(list(wuichi(list(map(int, input().split())), M, N)))

geori = 0
for i in range(T):
    if abs(sangjeom[i][0] - sangjeom[-1][0]) == N :
        geori += N + min(sangjeom[i][1] + sangjeom[-1][1], 2 * M - (sangjeom[i][1] + sangjeom[-1][1]))
    elif abs(sangjeom[i][1] - sangjeom[-1][1]) == M:
        geori += M + min(sangjeom[i][0] + sangjeom[-1][0], 2 * N - (sangjeom[i][0] + sangjeom[-1][0]))
    else:
        geori += abs(sangjeom[i][0] - sangjeom[-1][0]) + abs(sangjeom[i][1] - sangjeom[-1][1])
print(geori)