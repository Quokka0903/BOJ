import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def pre_to_post(s, e):
    if s > e:
        return
    
    i = s + 1
    r = pre[s]

    while i <= e:
        if pre[i] > r:
            break
        i += 1
    
    pre_to_post(s + 1, i - 1)
    pre_to_post(i, e)
    print(r)

pre = []
while True:
    try:
        pre.append(int(input()))

    except:
        break

pre_to_post(0, len(pre) - 1)