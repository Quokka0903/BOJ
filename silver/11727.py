res = [0] * 1001

res[1] = 1
res[2] = 3
res[3] = 5

for i in range(4, 1001):
    res[i] = res[i - 1] + (2 * res[i - 2])

print(res[int(input())] % 10007)