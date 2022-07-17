def time(i) :
    return (i * i)
sum = 0
N = list(input().split())
for i in range(len(N)) :
    sum += time(int(N[i]))
print(sum % 10)