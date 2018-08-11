while(True):
    n = int(input())
    if n == 0:
         break
    oe = []
    for i in range(n):
        e,p,q = map(int, input().split())
        for a in oe:
            if a[0] == e:
                a[1] += p*q
                continue
        oe.append([e,p*q])
    lis = [ a[0] for a in oe if a[1] >= 1000000]
    if len(lis):
        print("\n".join(str(l) for l in lis))
    else:
        print("NA")