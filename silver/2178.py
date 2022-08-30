d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

N, M = map(int, input().split())
miro = [input() for _ in range(N)]
moved = [[0] * M for _ in range(N)]

moved[0][0] = 1
stack = [[0, 0]]
while stack:
    
    s = stack.pop(0)

    if s[0] == (N - 1) and s[1] == (M - 1):
        print(moved[s[0]][s[1]])
        break

    for i in range(4):

        if 0 <= s[0] + d[i][0] < N and 0 <= s[1] + d[i][1] < M:

            if miro[s[0] + d[i][0]][s[1] + d[i][1]] == '1':
                
                if not moved[s[0] + d[i][0]][s[1] + d[i][1]]:
                    moved[s[0] + d[i][0]][s[1] + d[i][1]] = moved[s[0]][s[1]] + 1
                    stack.append([s[0] + d[i][0], s[1] + d[i][1]])
                elif moved[s[0] + d[i][0]][s[1] + d[i][1]] > moved[s[0]][s[1]] + 1:
                    moved[s[0] + d[i][0]][s[1] + d[i][1]] = moved[s[0]][s[1]] + 1
                    stack.append([s[0] + d[i][0], s[1] + d[i][1]])