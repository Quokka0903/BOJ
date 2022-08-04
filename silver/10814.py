T = int(input())

person = []
for i in range(T) :
    age, name = map(str, input().split())
    person.append([int(age), name])

temp = sorted(person, key = lambda x : (x[0]))

for ans in temp :
    print(ans[0], end=' ')
    print(ans[1])