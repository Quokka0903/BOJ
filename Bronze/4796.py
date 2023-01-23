cnt = 1
while True:
    L, P, V = map(int, input().split())
    if L + P + V == 0:
        break
    print(f'Case {cnt}:', ((V // P) * L) + min(V % P, L))
    cnt += 1