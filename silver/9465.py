import sys
input = sys.stdin.readline

for t in range(int(input())):
    N = int(input())
    jumsu = [list(map(int, input().split())) for _ in range(2)]
    
    for j in range(1, N):
        if j == 1:
          jumsu[0][j] += jumsu[1][j - 1]
          jumsu[1][j] += jumsu[0][j - 1]
        else:
          jumsu[0][j] += max(jumsu[1][j - 1], jumsu[1][j - 2])
          jumsu[1][j] += max(jumsu[0][j - 1], jumsu[0][j - 2])
    
    print(max(jumsu[0][N - 1], jumsu[1][N - 1]))