x, y = map(int, input().split())
day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

res = 0
if x >= 2:
    res += (sum(month[:x-1]) + y - 1) % 7
else:
    res += (y - 1) % 7

print(day[res])