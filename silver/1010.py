def makesite(n):
    res = 1
    for i in range(n):
        res *= (i + 1)
    return res


for _ in range(int(input())):
    N, M = map(int, (input().split()))
    
    print(makesite(M) // (makesite(N) * makesite((M - N))))