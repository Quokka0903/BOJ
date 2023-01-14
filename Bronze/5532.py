import math

L = int(input())
A = int(input())
B = int(input())
L -= max(math.ceil(A / int(input())), math.ceil(B / int(input())))

print(L)