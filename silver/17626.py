sq = [] 
for i in range(224):
    sq.append(i ** 2)

chk = int(input())

cnt = [0]
for i in range(1, chk + 1):
    cnt.append(i)
    for j in range(224):

        if i == sq[j]:
            cnt[i] = 1

        if i > sq[j]:
            cnt[i] = min(cnt[i], cnt[i - sq[j]] + 1)

        elif i < sq[j]:
            break

print(cnt[chk]) #시간초과라서 pypy3으로 채점.