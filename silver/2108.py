from collections import deque #미완
import sys
input = sys.stdin.readline

N = int(input())

do_math = deque()
dict = {}

sum = 0
for _ in range(N):
    num = int(input())
    
    if do_math:
        if num > do_math[-1]:
            do_math.append(num)
        elif num < do_math[0]:
            do_math.appendleft(num)
        else :
            cnt = 0
            while do_math and do_math[0] < num:
                do_math.rotate(-1)
                cnt += 1
            do_math.appendleft(num)
            do_math.rotate(cnt)
    else :
        do_math.append(num)

    sum += num
    
    if num not in dict:
        dict[num] = 1
    else :
        dict[num] += 1

max_time = 0
max_num = 0
for x in range(N):
    if dict.get(do_math[x]) >= max_time:
        max_time = dict.get(do_math[x])
        max_idx = x

bindo = 0
bin_cnt = 0
for y in range(0, x - 1, 1):
    if dict.get(do_math[y]) == max_time:
        bindo = do_math[y]
        bin_cnt += 1
    if bin_cnt == 2:
        break


print(round(sum/N))
print(do_math[N//2])
print(bindo)
print(do_math[-1] - do_math[0])