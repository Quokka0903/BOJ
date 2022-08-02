x, y = map(int, input().split())
N = int(input())
list_x = [0] * (x)
list_y = [0] * (y)
sero = []
garo = []
for i in range(N) :
    code, degree = map(int, input().split())
    if code == 0 :
        for j in range(len(list_y)) :
            if j == degree :
                list_y[j] += 1
    else :
        for j in range(len(list_x)) :
            if j == degree :
                list_x[j] += 1


count = 0
for j in range(len(list_x)) :
    if list_x[j] == 1:
        sero.append(count)
        count = 0
    count += 1
sero.append(count)
count = 0
for j in range(len(list_y)) :
    if list_y[j] == 1:
        garo.append(count)
        count = 0
    count += 1
garo.append(count)

print(max(garo) * max(sero))