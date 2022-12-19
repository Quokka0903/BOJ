sort_n = []
for _ in range(5):
    sort_n.append(int(input()))

print(sum(sort_n)//5)
print(sorted(sort_n)[2])