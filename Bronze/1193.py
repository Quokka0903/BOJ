n = int(input())

i = 1
while (i * (i + 1) // 2) < n:
    i += 1

chk = n - ((i - 1) * i // 2)
if i % 2 == 0:
    print(f'{chk}/{i - chk + 1}')
else:
    print(f'{i - chk + 1}/{chk}')