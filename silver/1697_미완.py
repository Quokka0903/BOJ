N, K = map(int, input().split())

sumba = []
for i in range(100001):
    sumba.append(abs(N - i))
#print(sumba[N : K + 1])

for i in range(100001):
    if i % 2 == 0:
        if i < 100000:
            sumba[i] = min(sumba[i - 1], sumba[i // 2], sumba[i + 1]) + 1
        else :
            sumba[i] = min(sumba[i - 1], sumba[i // 2]) + 1
    else: 
        if i < 100000:
            sumba[i] = min(sumba[i - 1], sumba[i + 1]) + 1
        else :
            sumba[i] = sumba[i - 1] + 1
            
#print(sumba[N : K + 1])
print(sumba[K])