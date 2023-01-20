N = int(input())
cmds = [input() for _ in range(N)]

res = ''
for i in range(len(cmds[0])):
    temp = ''
    for unit in cmds:
        if not temp:
            temp += unit[i]
        else:
            if temp == unit[i]:
                continue
            else:
                res += '?'
                break
    else:
        res += unit[i]
print(res)
