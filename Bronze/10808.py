strs = input()
cnt = [0] * 26
for unit in strs:
    cnt[ord(unit) - 97] += 1
print(*cnt)
