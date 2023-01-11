N = int(input())
strs = []
for _ in range(N):
    strs.append(input())

johab = []
for unit in sorted(strs):

    temp = []
    for comp in strs:
        if comp.startswith(unit):
            temp.append(comp)
    
    for check in johab:
        flag = 0
        for temp_str in temp:
            if temp_str in check:
                flag = 1
                break
        if flag:
            break
    else:        
        johab.append(temp)
    

ans = 0
if len(johab) == 1:
    ans += 1
else:
    for res in johab:
        if len(res) > 1:
            ans += len(res) - 1
        else:
            ans += len(res)

# print(johab)
print(ans)