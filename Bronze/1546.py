def fix(i) :
    return (i / M * 100)

T = int(input())
M = 0
av = 0
arr = list(map(int, input().split()))
for i in range(T) : 
    if M < arr[i] :
        M = arr[i]
arr = list(map(fix, arr))
for i in range(T) : 
    av += arr[i]
print ("%f" % (av / T))