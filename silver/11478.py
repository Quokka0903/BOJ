munza = input()
set_munza = set(munza)

for i in range(len(munza) + 1):
    for j in range(i + 1, len(munza) + 1):
        set_munza.add(munza[i:j])

print(len(set_munza))