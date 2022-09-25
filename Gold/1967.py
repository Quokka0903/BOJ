import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def zirum(node, giri):
    
    if not nodes[node]:
        return giri
    
    giris = []
    for i in range(len(nodes[node])):
        giris.append(zirum(nodes[node][i][0], nodes[node][i][1]))

    if len(giris) == 1:
        zirums.append(giris[0])
    else:
        s_giris = sorted(giris)
        zirums.append(s_giris[-1] + s_giris[-2]) # 굿~

    return (max(giris) + giri)

n = int(input())
nodes = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p,c , l = map(int, input().split())
    nodes[p].append([c, l])

zirums = []
root = 1
zirum(root, 0)

if zirums:
    print(max(zirums))
else:
    print(0)