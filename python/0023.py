n = int(input())
for _ in range(n):
    xa,ya,ra,xb,yb,rb = map(float, input().split())
    dr = ((xa-xb)**2+(ya-yb)**2)**0.5
    if rb > (ra+dr):
        print(-2)
        continue
    elif ra > (rb+dr):
        print(2)
        continue
    elif dr > (ra+rb):
        print(0)
        continue
    else:
        print(1)
