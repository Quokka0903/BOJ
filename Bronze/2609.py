a, b = map(int, input().split())
max_yaksu, min_besu = 0,0
for i in range(1, min(a, b)) :
    if a % i == 0 and b % i == 0 :
        max_yaksu = i
min_besu = a * b // max_yaksu

print(max_yaksu)
print(min_besu)