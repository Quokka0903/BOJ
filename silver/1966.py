from collections import deque
import sys

input = sys.stdin.readline

def my_max(a):
    max, cnt, res_cnt = 0, 0, 0
    for i in a:
        if max < i:
            max = i
            res_cnt = cnt
        cnt += 1
    return max, res_cnt


T = int(input())

for t in range(T):
    cnt = 1
    idx_ord = deque()
    N, idx = map(int, input().split())
    for i in range(N):
        idx_ord.append(i)
    printer = deque(list(map(int, input().split())))

    while True:
        # print(idx_ord)
        # print(printer)
        # print(my_max(printer))

        max, max_cnt = my_max(printer)
        printer.rotate(-max_cnt)
        idx_ord.rotate(-max_cnt)
        
        if idx_ord[0] == idx:
            break

        printer.popleft()
        idx_ord.popleft()
        cnt += 1
                
    print(cnt)