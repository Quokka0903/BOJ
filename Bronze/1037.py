import sys

input = sys.stdin.readline

yak = int(input())
yaks = sorted(list(map(int, input().split())))
print(yaks[0] * yaks[-1])