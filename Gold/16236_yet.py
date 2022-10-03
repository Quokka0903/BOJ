import collections, sys
input = sys.stdin.readline

N = int(input())
erhang = [list(map(int, input().split())) for _ in range(N)]
fishes = []

fish = 0
baby = 2
temp = 0
baby_idx = []
for y in range(N):
    for x in range(N):
        if erhang[y][x]:
            if erhang[y][x] == 9:
                baby_idx.extend([y, x])
                erhang[y][x] = 0
            else:
                fish += 1
                fishes.append(erhang[y][x])
fishes.sort()
print(fishes)
print(baby_idx)

def a_gi_sang_er(baby, temp, fish):
    if fish:
        visited = [[0] * N for _ in range(N)]
        stack = collections.deque([baby_idx + [0]])
        while stack:
            s = stack.popleft()
            print('s')
            print(s)
            visited[s[0]][s[1]] = 1

            for dy, dx in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                ny = s[0] + dy
                nx = s[1] + dx
                if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:

                    if erhang[ny][nx] <= baby:
                        if 0 < erhang[ny][nx] < baby:
                            fish -= 1
                            fishes.remove(erhang[ny][nx])
                            if fish == 0:
                                return s[2] + 1

                            temp += 1
                            if temp == baby:
                                baby += 1
                                temp = 0
                            
                            if temp < baby and fishes[0] >= baby:
                                return s[2] + 1

                            erhang[ny][nx] = 0
                            stack = collections.deque([[ny, nx, s[2] + 1]])
                            break
                        
                        stack.append([ny, nx, s[2] + 1])

            print('check')
            print(stack)
            print(baby)

    else:
        return 0

print(a_gi_sang_er(baby, temp, fish))