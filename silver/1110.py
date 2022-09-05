num = comp = input()
cnt = 0
while True:
    if int(num) < 10 and len(num) < 2:
        num = '0' + num
    temp = str(int(num[0]) + int(num[1]))
    num = num[-1] + temp[-1]
    cnt += 1
    if int(comp) == int(num):
        break
print(cnt)