from collections import defaultdict
N = int(input())

member = defaultdict()
for i in range(N):
   name, status = input().split()
   if (status == "enter") :
      member[name] = True
   else :
      member[name] = False

cnt = []
for unit in member:
   if member[unit] :
      cnt.append(unit)

print(*sorted(cnt)[::-1])