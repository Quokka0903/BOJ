import sys
input = sys.stdin.readline

S = list(input())
q = int(input())
list_char = [0] * 26
hap = []

for unit in S:
    if 97 <= ord(unit) <= 122:
        list_char[ord(unit) - 97] += 1
        hap.append(list_char[:])

for _ in range(q):
    a, l, r = input().split()
    ans = hap[int(r)][ord(a) - 97]
    if l != '0':
        ans -= hap[int(l) - 1][ord(a) - 97]
    print(ans)