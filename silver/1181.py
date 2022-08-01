T = int(input())
word_temp = set()
word_sort_temp = []
for _ in range(T) :
    word_temp.add(str(input()))
for text in word_temp :
    word_sort_temp.append([len(text), text])

ans = sorted(word_sort_temp, key= lambda x: (x[0], x[1]))

for res in ans :
    print(res[1])