whole = int(input())
chk = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    chk += a * b
if whole == chk:
    print('Yes')
else:
    print('No')