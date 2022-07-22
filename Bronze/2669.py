arr = [[0]*100 for _ in range(100)] # 또 배열 1만칸 만듬

for T in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2): 
        for j in range(y1, y2):
            arr[i][j] = 1 # 가로세로 1 할당
ans = 0
for i in arr:
    ans += i.count(1) # 전체에서 1 있는 것 카운트
print(ans)