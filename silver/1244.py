N = int(input())
list_switch = list(map(int, input().split()))

T = int(input())
for i in range(T) :
    S, turn = map(int, input().split())
    if S == 1:
        for i in range(len(list_switch)) :
            if (i + 1) % turn == 0 :
                list_switch[i] = abs(list_switch[i] - 1)
    
    
    else :
        idx = 0
        while turn + idx - 1 < N and turn - idx - 1 >= 0 :
            if idx == 0:
                list_switch[turn - 1] = abs(list_switch[turn - 1] - 1)
            elif list_switch[turn - idx - 1] == list_switch[turn + idx - 1] :
                list_switch[turn - idx - 1] = abs(list_switch[turn - idx - 1] - 1)
                list_switch[turn + idx - 1] = abs(list_switch[turn + idx - 1] - 1)
            else :
                break
            
            idx += 1

for i in list_switch :
    print((i), end =' ')