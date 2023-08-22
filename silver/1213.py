import sys
words = sys.stdin.readline().strip() 
alp_cnt = [0 for _ in range(27)]      

odd = 0                             
odd_index = -1                         

for word in words:
    alp_cnt[ord(word) - 65] += 1

for i in range(len(alp_cnt)):
    if alp_cnt[i] % 2 == 1:              
        odd += 1
        odd_index = i    
        if odd == 2:
            print("I'm Sorry Hansoo")
            exit()

alp_cnt[odd_index] -= 1           
for i in range(len(alp_cnt)):      
    if alp_cnt[i] % 2 != 1:
        for _ in range(alp_cnt[i] // 2):
            print(chr(i + 65), end="")

if odd_index != -1:
    print(chr(odd_index + 65), end="")    

for i in range(len(alp_cnt) - 1, -1, -1):
    if alp_cnt[i] % 2 != 1:
        for _ in range(alp_cnt[i] // 2):
            print(chr(i + 65), end="")