makdae = list(input())
answer = 0
stack = []

for i in range(len(makdae)):
    if makdae[i] == '(':
        stack.append('(')

    else:
        if makdae[i-1] == '(': 
            stack.pop()
            answer += len(stack)

        else:
            stack.pop() 
            answer += 1 

print(answer)