def rot_n(c, n):
    if 'a' <= c and c <= 'z':
        return chr((ord(c) - ord('a') + int(n)) % 26 + ord('a'))
    
    if 'A' <= c and c <= 'Z':
        return chr((ord(c) - ord('A') + int(n)) % 26 + ord('A'))
    
    return c

def rot(s, n):
    c = (rot_n(c, n) for c in s)
    return "".join(c)

while(True):
    try:
        s = input()
        for i in range(1,28):
            d = rot(s,i)
            if "this" in d.split() or "the" in d.split() or "that" in d.split():
                print(d)
    except:
        break