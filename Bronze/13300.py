import math

N, K = map(int, input().split())
student = [[0] * 6 for _ in range(2)]

for _ in range(1, N + 1):
    S, G = map(int, input().split())
    student[S][G - 1] += 1
        
room = 0
for i in student:
    for j in i:
        room += math.ceil(j / K)

print(room)