sunseo = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}
gualho = {'(' : ')'}

susik = input()
stack = []
for chk in susik:
    if ord(chk) >= 65 and ord(chk) <= 90:
        print(chk, end = '')
    else :
        if chk in sunseo:
            if stack:
                while stack and stack[-1] in sunseo and sunseo[stack[-1]] >= sunseo[chk]:
                    print(stack.pop(), end = '')
            stack.append(chk)
        else :
            if chk in gualho:
                stack.append(chk)
            else:
                while stack and stack[-1] != '(':
                    print(stack.pop(), end = '')
                stack.pop()
while stack:
    print(stack.pop(), end = '')
print()