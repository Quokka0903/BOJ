from sys import stdin

n = int(stdin.readline())

def temp_round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)
    
if n == 0:
    print(0)
else:
    nanido = [int(stdin.readline()) for _ in range(n)]
    
    idx = temp_round(n * 0.15)
    
    if idx:
        nanido = sorted(nanido)[idx : -idx]
    
    print(temp_round(sum(nanido)/(n - 2 * idx)))
