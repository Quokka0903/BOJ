C = list(map(int, input().split()))
if C == sorted(C) :
    print("ascending")
elif C == sorted(C, reverse = True) :
    print("descending")
else :
    print("mixed")