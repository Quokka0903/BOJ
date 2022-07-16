s = (input().upper()).replace(" ", "")
l = [0 for i in range(26)]
max0 = 0
max1 = 0
flag = 0
for i in range(len(s)) :
    l[(ord(s[i]) - 65)] += 1
for i in range(len(l)) :
    if max0 < l[i] :
        max0 = l[i]
        max1 = i
for i in range(len(l)) :
    if max0 == l[i] : 
        flag += 1
if flag > 1 :
    print("?")
else :
    print (chr(65 + max1))