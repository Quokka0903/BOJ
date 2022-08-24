N, r, c = map(int, input().split())


cnt = 0
while N > 0:
    cut = (2 ** N) // 2
    if N == 1:
        if r < cut  and c >= cut:
            cnt += 1

        elif r >= cut  and c < cut:
            cnt += 2

        elif r >= cut  and c >= cut:
            cnt += 3

    else :
        if r < cut  and c >= cut:
            cnt += (cut ** 2)
            c -= cut

        elif r >= cut  and c < cut:
            cnt += (cut ** 2) * 2
            r -= cut

        elif r >= cut  and c >= cut:
            cnt += (cut ** 2) * 3
            c -= cut
            r -= cut

    N -= 1

print(cnt)