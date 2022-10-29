prime = [False, False] +[True] * (123456 * 2 - 1)

for i in range(2, int((123456 * 2 - 1)**(0.5)) + 1):
    if prime[i]:
        for j in range(i ** 2, 123456 * 2 + 2, i):
            prime[j] = False


while True:
    N = int(input())
    if N == 0:
        break

    cnt = 0
    for i in range(N + 1, 2 * N + 1):
        if prime[i]:
            cnt += 1

    print(cnt)