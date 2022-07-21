dwarf = [0] * 9
suspect, sus1, sus2 = 0, 0, 0
for i in range(9) :
    dwarf[i] = int(input())
breaker = False
for i in range(9) :
    for j in range(i + 1, 9) :
        suspect = dwarf[i] + dwarf[j]
        if sum(dwarf) - suspect == 100 :
            dwarf[i], dwarf[j] = 0, 0
            breaker = True
            break
    if breaker == True :
        break
dwarf = sorted(dwarf)[2::]
for i in range(7) :
    print(dwarf[i])