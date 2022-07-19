N = int(input())
guess = 0
for i in range(N + 1) :
    x = list(map(int, str(i)))
    guess = i + sum(x)
    if guess == N :
        print(i)
        break
    if i == N :
        print(0)
