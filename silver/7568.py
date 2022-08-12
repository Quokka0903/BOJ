N = int(input())

dungchi = []
rate = []

for t in range(N):
    dungchi.append(list(map(int, input().split())))
    rate.append(1)

for i in range(len(dungchi)):
    for j in range(len(dungchi)):
        if i == j :
            continue
        else :
            if dungchi[i][0] > dungchi[j][0] and dungchi[i][1] > dungchi[j][1]:
                rate[j] += 1

print(*rate)