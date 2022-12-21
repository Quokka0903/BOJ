import sys
from collections import defaultdict
input = sys.stdin.readline

card = defaultdict()
N = int(input())
for unit in input().split() :
    card[unit] = 1

M = int(input())
def bool_check(a) :
    if a in card:
        return 1
    else:
        return 0
check = list(map(bool_check, input().split()))

print(*check)