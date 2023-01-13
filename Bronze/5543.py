menu = []
for _ in range(5):
    menu.append(int(input()))
burger = sorted(menu[:3])
drink = sorted(menu[3:])
print(burger[0] + drink[0] - 50)