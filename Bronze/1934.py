def big_factor (a, b):
    if b == 0:
        return a
    
    return big_factor(b, a % b)

for t in range(int(input())):
    a, b = map(int, input().split())
    g = big_factor(a, b)
    print(a * b // g)