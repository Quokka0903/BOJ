zumsu = 0
for _ in range(5):
    z = int(input())
    if z > 40:
        zumsu += z
    else:
        zumsu += 40
print(zumsu//5)