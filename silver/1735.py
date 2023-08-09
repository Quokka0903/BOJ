ax, ay = map(int, input().split(' '))
bx, by = map(int, input().split(' '))

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

cx = ax * by + bx * ay
cy = ay * by
res = gcd(cx, cy)
print(cx // res, cy // res)