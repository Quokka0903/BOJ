N, K = map(int, input().split())

def two_count(number):
    two_cnt = 0
    while number != 0:
        number = number // 2
        two_cnt += number
    return two_cnt

def five_count(number):
    five_cnt = 0
    while number != 0:
        number = number // 5
        five_cnt += number
    return five_cnt

two_cnt = two_count(N) - two_count(N - K) - two_count(K)

five_cnt = five_count(N) - five_count(N - K) - five_count(K)

print(min(two_cnt, five_cnt))