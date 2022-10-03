import sys
input = sys.stdin.readline


def tree(y1, x1, y2, x2):
    global res
    if y1 == y2 and x1 == x2:
        res += quad[y1][x1]
        return
        
    c0 = 0
    c1 = 0
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if quad[y][x] == '0':
                c0 += 1
            elif quad[y][x] == '1':
                c1 += 1
    
    if c0 and not c1:
        res += '0'
        return
        
    elif not c0 and c1:
        res += '1'
        return
    
    else:
        res += '('
        tree(y1, x1, y1 + (y2 - y1)//2, x1 + (x2 - x1)//2)
        tree(y1, x1 + (x2 - x1)//2 + 1, y1 + (y2 - y1)//2, x2)
        tree(y1 + (y2 - y1)//2 + 1, x1, y2, x1 + (x2 - x1)//2)
        tree(y1 + (y2 - y1)//2 + 1, x1 + (x2 - x1)//2 + 1, y2, x2)
        res += ')'
        return

N = int(input())
quad = [input() for _ in range(N)]
res = ''
tree(0, 0, N - 1, N - 1)

print(res)