idx = [0] * 42
cnt = 0
for i in range(10) : 
    idx[(int(input()) % 42)] += 1
for i in range(42) :
    if idx[i] > 0 :
        cnt += 1
print (cnt)