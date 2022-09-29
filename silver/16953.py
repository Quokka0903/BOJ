def make(num, cnt):
    if num == B:
        res.append(cnt)
        return
    
    if num > B:
        return
    
    make(num * 2, cnt + 1)
    make(int(str(num) + '1'), cnt + 1)

A, B = map(int, input().split())
res = []

make(A, 0)

if res:
    print(min(res) + 1)
else:
    print(-1)