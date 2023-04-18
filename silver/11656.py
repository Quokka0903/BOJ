n = input()
res = []
for i in range(len(n)):
    res.append(n[i:])

for unit in sorted(res):
    print(unit)