max = 0
temp = 0
idx = 0
for i in range(9) :
    temp = int(input())
    if (max < temp) : 
        max = temp
        idx = i + 1

print(max)
print(idx)