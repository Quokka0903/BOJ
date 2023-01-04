def gcd(a, b):
    while(b != 0):
        n = a%b
        a = b
        b = n
    return a

n = int(input())
r = list(map(int, input().split()))
for i in range(1, n):
    g = gcd(r[0], r[i])
    print(f'{r[0]//g}/{r[i]//g}')