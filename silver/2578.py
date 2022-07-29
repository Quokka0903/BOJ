bingo_pan = []
sut_za = []
for _ in range(5) :
    bingo_pan.extend(list(map(int, input().split())))

for _ in range(5) :
    sut_za.extend(list(map(int, input().split())))

su = 0
for i in range(len(sut_za)) :
    bingo_pan[bingo_pan.index(sut_za[i])] = 0
    cnt = 0
    if bingo_pan[0:5:1] == [0, 0, 0, 0, 0] :
        cnt += 1
    if bingo_pan[5:10:1] == [0, 0, 0, 0, 0] :
        cnt += 1
    if bingo_pan[10:15:1] == [0, 0, 0, 0, 0] :
        cnt += 1
    if bingo_pan[15:20:1] == [0, 0, 0, 0, 0] :
        cnt += 1
    if bingo_pan[20:25:1] == [0, 0, 0, 0, 0] :
        cnt += 1
    if bingo_pan[0:len(sut_za):5] == [0, 0, 0, 0, 0] :
        cnt += 1
    if bingo_pan[1:len(sut_za):5] == [0, 0, 0, 0, 0] :
        cnt += 1
    if bingo_pan[2:len(sut_za):5] == [0, 0, 0, 0, 0] :
        cnt += 1
    if bingo_pan[3:len(sut_za):5] == [0, 0, 0, 0, 0] :
        cnt += 1
    if bingo_pan[4:len(sut_za):5] == [0, 0, 0, 0, 0] :
        cnt += 1
    if bingo_pan[0:len(sut_za):6] == [0, 0, 0, 0, 0] :
        cnt += 1
    if bingo_pan[4:len(sut_za) - 1:4] == [0, 0, 0, 0, 0] :
        cnt += 1

    su += 1

    if cnt >= 3:
        print(su)
        break