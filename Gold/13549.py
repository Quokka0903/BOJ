import collections

N, K = map(int, input().split())

zari = [100003] * 100003
zari[N] = 0
stack = collections.deque([N])

flag = 0
while stack:
    s = stack.popleft()

    for t in [(s - 1), (s + 1), (s * 2)]:
        #print(t)
        #print(zari[s], zari[t])
        if 0 <= t < 100003:
            if t == s * 2:
                if zari[t] > zari[s]:
                    if t == K:
                        zari[t] = zari[s]
                        flag == 1
                        break

                    zari[t] = zari[s]
                    stack.append(t)

            else:
                if zari[t] > zari[s] + 1:
                    if t == K:
                        zari[t] = zari[s] + 1
                        flag == 1
                        break
                    
                    zari[t] = zari[s] + 1
                    stack.append(t)
        #print(stack)
    
    if flag:
        break

print(zari[K])