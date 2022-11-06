import sys
input = sys.stdin.readline
L, C = map(int, input().split())
strs = sorted(list(input().split()))
mos = ['a', 'e', 'i', 'o', 'u']

def make_pw (i, stack, mo, ja):
    if len(stack) == L:
        if mo >= 1 and ja >= 2:
            print(stack)
        return
    
    if i == C:
        return
    
    if strs[i] in mos:
        make_pw (i + 1, stack + strs[i], mo + 1, ja)
    else:
        make_pw (i + 1, stack + strs[i], mo, ja + 1)
    make_pw (i + 1, stack, mo, ja)

make_pw(0, '', 0, 0)