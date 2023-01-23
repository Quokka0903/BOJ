B = input()[::-1]

temp = 0
res = ''
for i, unit in enumerate(B):
    if i != 0  and i % 3 == 0:
        res = str(temp) + res
        temp = 0
    temp += int(unit) * (2 ** (i % 3))
    # print(i, unit, int(unit) ** (i % 3), temp)
else:
    res = str(temp) + res

print(res)