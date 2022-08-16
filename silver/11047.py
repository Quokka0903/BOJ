N, K = map(int, input().split())

money = []

for _ in range(N):
    money.append(int(input()))

total = K
sum_q = 0
for idx in range(N - 1, -1, -1) :
    
    sum_q += total // money[idx]
    total = total % money[idx]
    
print(sum_q)