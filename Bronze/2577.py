A = int(input())
B = int(input())
C = int(input())
time = str(A * B * C)
for i in range(10) : 
    print(time.count(str(i)))