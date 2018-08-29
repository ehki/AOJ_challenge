mi = 2000000
ma = 0
while(True):
    try:
        a = float(input())
        mi = min(a,mi)
        ma = max(a,ma)
    except:
        print(ma-mi)
        break
