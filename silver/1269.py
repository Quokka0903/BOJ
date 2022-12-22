A, B = map(int, input().split())

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

print(A + B - len(set_a & set_b) * 2)