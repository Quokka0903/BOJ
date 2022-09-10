n = int(input())
cnt = n
for i in range(n):
    strs = input()
    for j in range(len(strs) - 1):
        if strs[j] == strs[j + 1]:
            pass
        elif strs[j] in strs[j + 1:]: 
            cnt -= 1
            break
print(cnt)