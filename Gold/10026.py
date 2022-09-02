from collections import deque
from pprint import pprint
import sys

input = sys.stdin.readline

N = int(input())

grim = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

union = 0
for x in range(N):
    for y in range(N):
        if grim[y][x] == 'B':
            if visited[y][x] == 0:
                union += 1
                stack = deque()
                stack.append((y, x))
                while stack:
                    s = stack.pop()
                    visited[s[0]][s[1]] = 1
                    for d in range(4):
                        if 0 <= (s[0] + delta[d][0]) < N and 0 <= (s[1] + delta[d][1]) < N:
                            if grim[s[0] + delta[d][0]][s[1] + delta[d][1]] == 'B':
                                if visited[s[0] + delta[d][0]][s[1] + delta[d][1]] == 0:
                                    stack.append((s[0] + delta[d][0], s[1] + delta[d][1]))

#pprint(visited)

yak_union = 0
for x in range(N):
    for y in range(N):
        if grim[y][x] == 'R' or grim[y][x] == 'G':
            if visited[y][x] == 0:
                yak_union += 1
                stack = deque()
                stack.append((y, x))
                while stack:
                    s = stack.pop()
                    visited[s[0]][s[1]] = 2
                    for d in range(4):
                        if 0 <= (s[0] + delta[d][0]) < N and 0 <= (s[1] + delta[d][1]) < N:
                            if grim[s[0] + delta[d][0]][s[1] + delta[d][1]] == 'R' or grim[s[0] + delta[d][0]][s[1] + delta[d][1]] == 'G':
                                if visited[s[0] + delta[d][0]][s[1] + delta[d][1]] == 0:
                                    stack.append((s[0] + delta[d][0], s[1] + delta[d][1]))

#pprint(visited)

r_union = 0
for x in range(N):
    for y in range(N):
        if grim[y][x] == 'R':
            if visited[y][x] == 2:
                r_union += 1
                stack = deque()
                stack.append((y, x))
                while stack:
                    s = stack.pop()
                    visited[s[0]][s[1]] = 1
                    for d in range(4):
                        if 0 <= (s[0] + delta[d][0]) < N and 0 <= (s[1] + delta[d][1]) < N:
                            if grim[s[0] + delta[d][0]][s[1] + delta[d][1]] == 'R':
                                if visited[s[0] + delta[d][0]][s[1] + delta[d][1]] == 2:
                                    stack.append((s[0] + delta[d][0], s[1] + delta[d][1]))

#pprint(visited)

g_union = 0
for x in range(N):
    for y in range(N):
        if grim[y][x] == 'G':
            if visited[y][x] == 2:
                g_union += 1
                stack = deque()
                stack.append((y, x))
                while stack:
                    s = stack.pop()
                    visited[s[0]][s[1]] = 1
                    for d in range(4):
                        if 0 <= (s[0] + delta[d][0]) < N and 0 <= (s[1] + delta[d][1]) < N:
                            if grim[s[0] + delta[d][0]][s[1] + delta[d][1]] == 'G':
                                if visited[s[0] + delta[d][0]][s[1] + delta[d][1]] == 2:
                                    stack.append((s[0] + delta[d][0], s[1] + delta[d][1]))
#pprint(visited)
print(union + r_union + g_union, union + yak_union)