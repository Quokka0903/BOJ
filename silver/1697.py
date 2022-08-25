N, K = map(int, input().split())

sumba = []
for i in range(100003):
    sumba.append(abs(N - i))
#print(sumba[N : K + 1])

for i in range(N - 1, K + 2):
    
    sumba[i] = min(sumba[i - 1] + 1, sumba[i])

    if i % 2 == 0:
        sumba[i] = min(sumba[i // 2] + 1, sumba[i])
    else: 
        sumba[i] = min(sumba[i // 2] + 2, sumba[i // 2 + 1] + 2, sumba[i])
            
#print(sumba[N : K + 1])
print(sumba[K])