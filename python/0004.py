while(True):
    try:
        a,b,c,d,e,f = map(float, input().split())
        y = (a*f-c*d)/(a*e-b*d)
        x = (c-b*y)/a
        print("%.3f %.3f"%(x,y))
    except:
        break