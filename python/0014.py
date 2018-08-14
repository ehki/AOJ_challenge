while(True):
    try:
        d = int(input())
        r = 0
        for p in range(0,600,d):
            r += d*p**2
        print(r)
    except:
        break
