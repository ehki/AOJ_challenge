while(True):
    try:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        h = [c-d for c,d in zip(a,b)].count(0)
        v = sum([a.count(d) for d in b]) - h
        print(h,v)
    except:
        break