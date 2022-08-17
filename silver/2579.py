T = int(input())
scores = [0] * (T + 2)
temp = [0] * (T + 2)

for i in range(T):
    scores[i] = int(input())

temp[0] = scores[0]
temp[1] = scores[1] + scores[0]
temp[2] = scores[2] + max(scores[0], scores[1])


for idx in range(3, T):
    temp[idx] = scores[idx] + max(scores[idx - 1]  + temp[idx - 3], temp[idx - 2])


print(temp)
print(temp[T - 1])