from math import sin,cos
x,y,t = 0,0,90
while(True):
    d,a = map(int,input().split(","))
    if d==0 and a==0:
        print(int(x))
        print(int(y))
        break
    x += d*cos(t/180*3.141592)
    y += d*sin(t/180*3.141592)
    t -= a
