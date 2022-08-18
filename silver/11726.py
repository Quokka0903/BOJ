res = [0] * 1001

res[1] = 1
res[2] = 2

for i in range(3, 1001):
    res[i] = res[i - 1] + res[i - 2]

print(res[int(input())] % 10007)