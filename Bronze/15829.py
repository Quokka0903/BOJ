T = int(input())
str = str(input())
ans = 0
M = 1234567891
for i in range(T) :
    ans += (ord(str[i]) - 96)* 31**i
print (ans % M)