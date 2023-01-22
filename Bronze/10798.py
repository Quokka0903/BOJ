garo = []
for _ in range(5):
    garo.append(input())

for i in range(15):
    for j in range(5):
        if len(garo[j]) < (i + 1):
            continue
        print(garo[j][i], end='')