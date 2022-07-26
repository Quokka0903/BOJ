def set_dice(list, end, idx) :
    list_temp = []
    if idx == 0 : 
        end = list[5] # 입력받은 배열에서 0번의 맞은편은 5번
        list_temp.extend(list[1:5]) # 나머지 배열을 추가
    elif idx == 1 :
        end = list[3] # 입력받은 배열에서 1번의 맞은편은 3번
        list_temp.append(list[0]) # 나머지 배열을 추가
        list_temp.append(list[2])
        list_temp.append(list[4])
        list_temp.append(list[5])
    elif idx == 2 :
        end = list[4] # 입력받은 배열에서 2번의 맞은편은 4번
        list_temp.append(list[0]) # 나머지 배열을 추가
        list_temp.append(list[1])
        list_temp.append(list[3])
        list_temp.append(list[5])
    elif idx == 3 :
        end = list[1] # 입력받은 배열에서 3번의 맞은편은 1번
        list_temp.append(list[0]) # 나머지 배열을 추가
        list_temp.append(list[2])
        list_temp.append(list[4])
        list_temp.append(list[5])
    elif idx == 4 :
        end = list[2] # 입력받은 배열에서 4번의 맞은편은 2번
        list_temp.append(list[0]) # 나머지 배열을 추가
        list_temp.append(list[1])
        list_temp.append(list[3])
        list_temp.append(list[5])
    elif idx == 5 :
        end = list[0]  # 입력받은 배열에서 5번의 맞은편은 0번
        list_temp.extend(list[1:5]) # 나머지 배열을 추가
    
    return(list_temp, end) # 나머지 배열과 주사위 천장 수를 반환

T = int(input())
list_dice = [list(map(int,input().split())) for _ in range(T)]
end, max_ans = 0, 0
list_temp = []
for i in range(6) :
    max_temp = 0 # 임시 최댓값 초기화
    list_temp, end = set_dice(list_dice[0], end, i)
    max_temp += max(list_temp) # 바닥과 천장 수 뺀 나머지 배열에서 가장 큰 수 추가
    for j in range(1, T) : # 나머지 주사위도 똑같은 순서를 밟음
        list_temp, end = set_dice(list_dice[j], end, list_dice[j].index(end))
        max_temp += max(list_temp)
    if max_temp > max_ans : # 최댓값 최신화
        max_ans = max_temp

print(max_ans)