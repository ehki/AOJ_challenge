while(True):
    n = int(input())
    d = []
    if not n:
        break
    while(n):
        d.append(n%8)
        n = int(n/8)
    f = [0,1,2,3,5,7,8,9]
    for e in d[::-1]:
        print(f[e],end="")
    print()
    
