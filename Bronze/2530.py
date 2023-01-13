si, bun, cho = map(int, input().split())
time = int(input())

if time >= 3600:
    si += time // 3600
    time %= 3600
if time >= 60:
    bun += time // 60
    time %= 60
if time >= 1:
    cho += time

if cho > 59:
    bun += cho // 60
    cho %= 60
if bun > 59:
    si += bun // 60
    bun %= 60
if si > 23:
    si %= 24


print(si, bun, cho)