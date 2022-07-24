T = int(input())

result = []
for i in range(T) :
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))
    score_A = [0] * 4
    score_B = [0] * 4
    for i in range(1, list_A[0] + 1) :
        score_A[4 - list_A[i]] += 1
    for i in range(1, list_B[0] + 1) :
        score_B[4 - list_B[i]] += 1
    if score_A == score_B :
        result.append('D')
    else :
        for i in range(4) :
            if score_A[i] == score_B[i] :
                continue
            else :
                result.append('A') if score_A[i] > score_B[i] else result.append('B')
                break
for i in range(T) :
    print(result[i])