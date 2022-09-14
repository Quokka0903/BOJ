def preorder(n):
    print(val[n], end='')

    if ch1[n].isalpha():
        preorder(dic_chr[ch1[n]])
    if ch2[n].isalpha():
        preorder(dic_chr[ch2[n]])
    

def inorder(n):
    if ch1[n].isalpha():
        inorder(dic_chr[ch1[n]])

    print(val[n], end='')

    if ch2[n].isalpha():
        inorder(dic_chr[ch2[n]])


def postorder(n):
    if ch1[n].isalpha():
        postorder(dic_chr[ch1[n]])
    if ch2[n].isalpha():
        postorder(dic_chr[ch2[n]])
    print(val[n], end='')


V = int(input())
dic_chr = {}
ch1 = [''] * (V + 1)
ch2 = [''] * (V + 1)
val = [''] * (V + 1)
for i in range(V):
    p, c1, c2 = input().split()
    dic_chr[p] = i + 1
    val[i + 1] += p
    if c1.isalpha():
        ch1[dic_chr[p]] += c1
    if c2.isalpha():
        ch2[dic_chr[p]] += c2

root = 1

preorder(root)
print()
inorder(root)
print()
postorder(root)
print()