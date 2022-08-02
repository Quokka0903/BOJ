N = int(input())

list_num = list(map(int,input().split()))

prime = 0
for i in list_num :
    count = 0
    for j in range(1, i + 1) :
        if i % j == 0:
            count += 1
    if count == 2:
        prime += 1

print(prime)