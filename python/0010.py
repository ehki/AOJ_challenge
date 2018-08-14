n = int(input())
for _ in range(n):
    x1,y1,x2,y2,x3,y3 = map(float, input().split())
    gx = (x1+x2+x3)/3
    gy = (y1+y2+y3)/3
    G=( y2*x1-y1*x2 +y3*x2-y2*x3 +y1*x3-y3*x1 )
    Xc= ((x1*x1+y1*y1)*(y2-y3)+(x2*x2+y2*y2)*(y3-y1)+(x3*x3+y3*y3)*(y1-y2))/(2*G)
    Yc=-((x1*x1+y1*y1)*(x2-x3)+(x2*x2+y2*y2)*(x3-x1)+(x3*x3+y3*y3)*(x1-x2))/(2*G)
    r = ( (x1 - Xc) * (x1 - Xc) + (y1 - Yc) * (y1 - Yc) )**0.5
    print("%.3f %.3f %.3f"%(Xc,Yc,r))
