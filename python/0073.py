while True:
    x = float(input())
    h = float(input())
    if x == 0 and h == 0: break
    print("%.6f"%(x**2+x*2*(h**2+(x/2)**2)**0.5))