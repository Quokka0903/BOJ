import sys
input = sys.stdin.readline

N = int(input())
acche = list(map(int, input().split()))

left = 0
right = N - 1
min_cha = abs(acche[left] + acche[right])
min_left = 0
min_right = N - 1

while left < right and acche[left] + acche[right] != 0:
    #print(min_cha)
    #print(min_left)
    #print(min_right)
    #print(left, right)
    if acche[left] + acche[right] > 0:
        if min_cha > abs(acche[left] + acche[right]):
            min_cha = abs(acche[left] + acche[right])
            min_left = left
            min_right = right
        right -= 1
    elif acche[left] + acche[right] < 0:
        if min_cha > abs(acche[left] + acche[right]):
            min_cha = abs(acche[left] + acche[right])
            min_left = left
            min_right = right

        left += 1
    else:
        break

if left != right and acche[left] + acche[right] == 0:
    print(f'{acche[left]} {acche[right]}')
else:
    print(f'{acche[min_left]} {acche[min_right]}')