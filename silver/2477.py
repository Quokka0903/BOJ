chamoi = int(input()) # 참외갯수
list_melon = [list(map(int, input().split())) for _ in range(6)]
x_max, x_min, y_max, y_min = 0, 0, 0, 0 # 최댓값, 최솟값 초기화
x_max_idx, y_max_idx = 0, 0 # 최댓값 인덱스 초기화
bat = 0 # 밭넓이 초기화
for i in range(6) :
    if list_melon[i][0] == 1 or list_melon[i][0] == 2 : # 높이 최댓값
        if y_max < list_melon[i][1] :
            y_max = list_melon[i][1]
            y_max_idx = i
    elif list_melon[i][0] == 3 or list_melon[i][0] == 4 : # 너비 최댓값
        if x_max < list_melon[i][1] :
            x_max = list_melon[i][1]
            x_max_idx = i

x_min = abs(list_melon[(y_max_idx - 1) % 6][1] - list_melon[(y_max_idx + 1) % 6][1])
y_min = abs(list_melon[(x_max_idx - 1) % 6][1] - list_melon[(x_max_idx + 1) % 6][1])

# 각 최댓값 변의 앞뒤 변은 무조건 최댓값 변과  한 변이므로,
# 두 변의 차의 절댓값이 곧 최솟값 변이 된다.

bat = (x_max * y_max) - (x_min * y_min)
print(bat * chamoi)