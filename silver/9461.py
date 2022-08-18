padoban = [0] * 101

padoban[1] = 1
padoban[2] = 1
padoban[3] = 1
padoban[4] = 2
padoban[5] = 2
padoban[6] = 3
padoban[7] = 4
padoban[8] = 5
padoban[9] = 7
padoban[10]= 9

for i in range(11, 101):
    padoban[i] = padoban[i - 1] + padoban[i - 5]

T = int(input())

for t in range(T):
    print(padoban[int(input())])