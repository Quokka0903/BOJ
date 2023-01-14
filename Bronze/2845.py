L, P = map(int,input().split())
chamga = list(map(int, input().split()))

for unit in chamga:
    print(unit - L * P, end=" ")