n = int(input())
gyp = []
gyp = list(map(int, input().rstrip().split()))
gyp.sort()
print(gyp[(n-1)//2])