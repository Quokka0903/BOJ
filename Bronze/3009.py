from collections import defaultdict
a = defaultdict()
b = defaultdict()

for _ in range(3) :
    A, B = map(int, input().split())
    if A in a:
        a[A] += 1
    else:
        a[A] = 1
    
    if B in b:
        b[B] += 1
    else:
        b[B] = 1

for unit in a:
    if a[unit] == 1:
        print(unit, end=' ')

for unit in b:
    if b[unit] == 1:
        print(unit)
