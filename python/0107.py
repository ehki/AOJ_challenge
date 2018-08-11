while(True):
    d,w,h = map(int, input().split())
    if d == 0 and w == 0 and h == 0:
        break
    l = min(d*d+w*w,w*w+h*h,h*h+d*d)
    n = int(input())
    for i in range(n):
        r = int(input())
        if 4*r*r > l:
            print("OK")
        else:
            print("NA")