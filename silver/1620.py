import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dogam = []
dogam_dic = {}

for i in range(N):
    pokemon = input().rstrip()
    dogam.append(pokemon)
    dogam_dic[pokemon] = i

for j in range(M):
    chk = input().rstrip()

    if chk.isalpha():
        print(dogam_dic[chk] + 1)
    elif chk.isdigit():
        print(dogam[int(chk) - 1])