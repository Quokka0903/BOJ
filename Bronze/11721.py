alpha = input()

for i in range(len(alpha) // 10):
    print(alpha[i * 10 : i * 10 + 10])

if len(alpha) % 10:
    print(alpha[-1 * (len(alpha) % 10) :])