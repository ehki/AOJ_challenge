a = []
while(True):
    n = int(input())
    if n == 0:
        break
    a.append(n)
    if len(a) == 5:
        uni = set(a)
        if len(uni) == 2 and 1 in uni and 2 in uni:
            for b in a: print(2 if b == 2 else 1)
        elif len(uni) == 2 and 2 in uni and 3 in uni:
            for b in a: print(2 if b == 3 else 1)
        elif len(uni) == 2 and 3 in uni and 1 in uni:
            for b in a: print(2 if b == 1 else 1)
        else:
            for _ in range(5): print(3)
        a = []
