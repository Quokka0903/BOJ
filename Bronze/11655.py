unit = input()

def rot(chars):
    if 65 <= ord(chars) <= 90:
        if ord(chars) + 13 > 90:
            return chr(65 + (ord(chars) - 78))
        else:
            return chr(ord(chars) + 13 )
    elif 97 <= ord(chars) <= 122:
        if ord(chars) + 13 > 122:
            return chr(97 + (ord(chars) - 110))
        else:
            return chr(ord(chars) + 13)
    else:
        return chars


for word in unit:
    print(rot(word), end='')