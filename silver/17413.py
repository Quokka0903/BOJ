import sys
words = list(sys.stdin.readline().rstrip())

i = 0
here = 0
while i < len(words):
    if words[i] == "<":
        i += 1 
        while words[i] != ">":
            i += 1 
        i += 1
    elif words[i].isalnum():
        here = i
        while i < len(words) and words[i].isalnum():
            i+=1
        temp = words[here:i]
        temp.reverse()      
        words[here:i] = temp
    else:                  
        i+=1               

print("".join(words))